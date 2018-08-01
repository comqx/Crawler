
from flask import Flask,request,render_template,session,jsonify
import requests,time,re
from bs4 import BeautifulSoup
import json
app=Flask(__name__)
app.debug=True
app.secret_key='sadfasfasd'

def xml_parser(text):
    dic={}
    soup=BeautifulSoup(text,'html.parser')
    div=soup.find(name='error')
    #找到error下面的孩子
    for item in div.find_all(recursive=False): #只找div下面的儿子
        dic[item.name]=item.text
    return dic

@app.route('/',methods=['GET','POST'])
def login():
    if request.method=='GET':
        timer=str(int(time.time()*1000))
        qcloud_url='https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&redirect_uri=https%3A%2F%2Fwx.qq.com%2Fcgi-bin%2Fmmwebwx-bin%2Fwebwxnewloginpage&fun=new&lang=zh_CN&_={timer}'.format(timer=timer)
        ret=requests.get(qcloud_url)
        qcode=re.findall('uuid = "(.*)";',ret.text)[0]
        # print(qcode)
        session['qcode']=qcode
        # print(session)
        return render_template('login.html',qcode=qcode)

@app.route('/check_login')
def  check_login():
    response={'code':408}
    qcode=session.get('qcode')
    ctime=str(int(time.time() * 1000))
    #发送get请求检测是否已经扫码登录
    check_url='https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid={0}&tip=0&r=-802102026&_={1}'.format(qcode,ctime)
    reter=requests.get(check_url)
    # print(reter.text)
    if 'code=201' in reter.text:
        #已经扫码，获取用户头像
        src=re.findall("userAvatar = '(.*)';",reter.text)[0]
        response['code']=201
        response['src']=src
    elif 'code=200' in reter.text:
        #确认登录
        redirect_uri=re.findall('redirect_uri="(.*)";',reter.text)[0]
        redirect_uri=redirect_uri+'&fun=new&version=v2'
        print(redirect_uri)
        ticket_ret=requests.get(redirect_uri)
        # print(ticket_ret.text)
        ticket_dict=xml_parser(ticket_ret.text)
        print(ticket_dict)
        #用户未少扫码：
        session['ticket_dict']=ticket_dict
        #获取cookie
        session['ticket_cookie']=ticket_ret.cookies.get_dict()
        response['code']=200
    return jsonify(response)


@app.route('/index')
def index():
    '''
    用户数据的初始化：
    :return:
    '''
    ticket_dict=session.get('ticket_dict')
    print(ticket_dict)
    init_url='https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxinit?r=-1095755569&pass_ticket={0}'.format(ticket_dict.get('pass_ticket'))
    print(init_url)
    data_dict={
            'BaseRequest':{
            'DeviceID': 'e688944292743470',
            'Sid': ticket_dict.get('wxsid'),
            'Skey': ticket_dict.get('skey'),
            'Uin': ticket_dict.get('wxuin'),
        },
    }
    init_ret=requests.post(
        url=init_url,
        json=data_dict,#或者下面的传data，但是必须要在headers中指定返回的结果
        # data=json.dumps(data_dict),
        # headers={
        #     'Content-Type':'application/json'
        # }
    )
    init_ret.encoding='utf-8'
    # print(init_ret.text)
    user_dict=init_ret.json()
    print(user_dict)
    for user in user_dict['ContactList']:
        print(user['NickName'])
    #把用户的信息放到session中
    session['current_user']=user_dict['User']
    session['sync_key']=user_dict['SyncKey']
    return render_template('index.html',user_dict=user_dict,)


@app.route('/get_img')
def get_img():
    #获取头像：
    #获取ticket的cookie信息
    ticket_cookie=session.get('ticket_cookie')
    #获取上一个请求的用户信息
    current_user=session.get('current_user')
    print(current_user)
    head_url='https://wx.qq.com'+current_user['HeadImgUrl']
    img_ret=requests.get(
        head_url,
        cookies=ticket_cookie,
        headers={'Content-Type':'imge/jpeg'}
    )
    print(img_ret.text)
    return img_ret.content

@app.route('/user_list')
def user_list():
    ticket_dict=session.get('ticket_dict')
    ticket_cookie=session.get('ticket_cookie')

    ctime=int(time.time() * 1000)
    skey=ticket_dict.get('skey')
    user_list_url='https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxgetcontact?lang=zh_CN&r={0}&seq=0&skey={1}'.format(ctime,skey)

    r1=requests.get(user_list_url,cookies=ticket_cookie)
    r1.encoding='utf-8'
    wx_user_dict=r1.json() #拿到一个地址
    # for item in wx_user_dict:
    #     print(item)
    print(wx_user_dict['MemberCount'])
    for item in wx_user_dict['MemberList']:
        print(item['NickName'],'',item['Signature'])

    return render_template('user_list.html',wx_user_dict=wx_user_dict)

#发送消息
@app.route('/send',methods=['GET','POST'])
def send():
    if request.method=='GET':
        return render_template('send.html')
    current_user=session['current_user']
    from_user=current_user['UserName']
    to=request.form.get('to')
    #前端传进来的内容
    content=request.form.get('content')
    ctime = str(int(time.time() * 1000))
    ticket_dict = session['ticket_dict']
    msg_url='https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&pass_ticket={0}'.format(ticket_dict['pass_ticket'])
    data_dict = {"BaseRequest":
                    {"Uin": ticket_dict['wxuin'],
                     "Sid": ticket_dict['wxsid'],
                     "Skey": ticket_dict['skey'],
                     "DeviceID": "e688944292743470"},
                "Msg":
                    {"Type": 1,
                     "Content": content,
                     "FromUserName": from_user,
                     "ToUserName": to,
                     "LocalID": ctime,
                     "ClientMsgId": ctime
                     },
                "Scene": 0}
    ret=requests.post(
        url=msg_url,
        # json=data_dict,
        #在传送中文的时候，如果只dumps后，使用socket发送，socket发送会把data转换为二进制
        data=bytes(json.dumps(data_dict,ensure_ascii=False),encoding='utf-8')
    )
    print(ret.text)
    return ret.text

@app.route('/get_msg',methods=['GET','POST'])
def get_msg():
    #检测是否有新消息到来
    sync_url='https://webpush.wx.qq.com/cgi-bin/mmwebwx-bin/synccheck'
    # sync_data_list=[]
    synckey=session['sync_key']
    print(synckey)
    ticket_dict = session['ticket_dict']
    nid=int(time.time())
    for item in synckey['List']:
        print(item)
    sync_dict ={"BaseRequest":
                      {"Uin": ticket_dict['wxuin'],
                       "Sid": ticket_dict['wxsid'],
                       "Skey": ticket_dict['skey'],
                       "DeviceID": "e688944292743470"},
                 "SyncKey": synckey,
                 "r": nid}

    ticket_dict=session.get('ticket_dict')
    ticket_cookie=session.get('ticket_cookie')
    get_ret=requests.get(sync_url,params=sync_dict,cookies=ticket_cookie)
    # print(get_ret.txt)
    return  get_ret.text

#发送消息
@app.route('/send_for',methods=['GET','POST'])
def send_for():
    if request.method=='GET':
        current_user=session['current_user']
        from_user=current_user['UserName']
        # to='@3090cbb300de377fcfad85bb3120a7a6a3c57786f4bffc1b88dc7bc7f06e4621'
        to='@b1d1e43b84e91851dcf19620f4fd4a8f'
        # to='@1678f4fd7c4981fbcc0fa001d103d61dac7669df6657b2a112e9e17753e89302'
        #前端传进来的内容
        for i in range(1,100):
            time.sleep(5)
            content='{0}、我叫丁凯,我是是傻逼'.format(i)
            ctime = str(int(time.time() * 1000))
            ticket_dict = session['ticket_dict']
            msg_url='https://wx.qq.com/cgi-bin/mmwebwx-bin/webwxsendmsg?lang=zh_CN&pass_ticket={0}'.format(ticket_dict['pass_ticket'])
            data_dict = {"BaseRequest":
                            {"Uin": ticket_dict['wxuin'],
                             "Sid": ticket_dict['wxsid'],
                             "Skey": ticket_dict['skey'],
                             "DeviceID": "e688944292743470"},
                        "Msg":
                            {"Type": 1,
                             "Content": content,
                             "FromUserName": from_user,
                             "ToUserName": to,
                             "LocalID": ctime,
                             "ClientMsgId": ctime
                             },
                        "Scene": 0}
            ret=requests.post(
                url=msg_url,
                # json=data_dict,
                #在传送中文的时候，如果只dumps后，使用socket发送，socket发送会把data转换为二进制
                data=bytes(json.dumps(data_dict,ensure_ascii=False),encoding='utf-8')
            )
            print(ret.text)
    return 'end'


if __name__ == '__main__':
    app.run()

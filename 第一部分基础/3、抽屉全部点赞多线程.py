#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:lqx
import requests
from bs4 import BeautifulSoup
from threading import Thread,current_thread

#开启多线程点赞

#第一次访问网页，得到为认证的cookies：
response_int=requests.get(
    url='https://dig.chouti.com/',
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }

)
r1_cookie_dict=response_int.cookies.get_dict()



#携带未认证的cookies，去登录注册
response_login=requests.post(
    url='https://dig.chouti.com/login',
    data={
        'phone':'8618311166263',
        'password':'liu890892',
        'oneMonth':'1',

    },
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    },
    cookies=r1_cookie_dict
)

def abc(i):
    response_int=requests.get(
        url='https://dig.chouti.com/all/hot/recent/%s'%i,
        headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
        }

    )
    #格式化html格式网页，转换为对象的方式
    soup=BeautifulSoup(response_int.text,'html.parser')
    div=soup.find(id='content-list')
    items=div.find_all(attrs={'class':'item'})

    for item in items:
        #获取每一个新闻的id：
        tag=item.find(attrs={'class':'part2'})
        nid=tag.get('share-linkid')
        # print(nid)

        # #根据每一个nid,去点赞
        response=requests.post(
            url='https://dig.chouti.com/link/vote?linksId=%s'%nid,
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
            },
            cookies=r1_cookie_dict
        )
        print(response.text)

        #取消点赞
        response = requests.post(
            url='https://dig.chouti.com/vote/cancel/vote.do',
            headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
            },
            cookies=r1_cookie_dict,
            data={'linksId': nid}
        )
        print(response.text)

for i in range(1,20):
    t1=Thread(target=abc,args=(i,))   #启动一个线程，把建立的连接发送给这个线程去执行，实现并发
    t1.start()


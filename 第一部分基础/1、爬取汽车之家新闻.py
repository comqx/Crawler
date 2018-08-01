#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:lqx

import requests
from bs4 import BeautifulSoup

#下载页面
ret=requests.get(url='https://www.autohome.com.cn/news/')
# print(ret.apparent_encoding)  #自动查找url的编码
# print(ret.content) #二进制
# ret.encoding='GBK'
ret.encoding=ret.apparent_encoding
# print(ret.text)

#解析：获取想要的指定内容 beautifulsoup4
soup=BeautifulSoup(ret.text,'html.parser') #html.parser和lxml用途相同，但是lxml速度比较快，
div=soup.find(name='div',id='auto-channel-lazyload-article') #找到匹配成功的第一个
li_list=div.find_all(name='li') #找到全部
# print(li_list)
for li in li_list:
    h3=li.find(name='h3')
    if not h3:continue
    p=li.find(name='p')
    a=li.find('a')
    # print(a.attrs)  #拿到他的属性
    img=li.find('img')
    # print(h3.text)
    # print(p.text) #拿到他的信息
    # print(a.get('href')) #拿到他的地址
    src=img.get('src')
    file_name=src.rsplit('__',maxsplit=1)[1]
    ret_img=requests.get(url='https:'+src)
    with open(file_name,'wb') as f:
        f.write(ret_img.content)
    # print(ret_img.content)
    # print('=='*15)





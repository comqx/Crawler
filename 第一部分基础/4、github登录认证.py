#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:lqx



#from表单提交数据

import requests
from bs4 import BeautifulSoup

response_in=requests.get(
    url='https://github.com/login',
    headers={
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    }
)
# print(response_in.text)
cookie=response_in.cookies.get_dict()
soup=BeautifulSoup(response_in.text,'html.parser')
token=soup.find(name='input',attrs={'name':'authenticity_token'}).get('value')
print(token)


response_login=requests.post(
    url='https://github.com/session',
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    },
    data={
        'commit':'Sign in',
        'utf8':'√',
        'authenticity_token':token,
        'login':'18311166263@163.com',
        'password':'liu890892'
    },
    cookies=cookie
)
print(response_login.text)
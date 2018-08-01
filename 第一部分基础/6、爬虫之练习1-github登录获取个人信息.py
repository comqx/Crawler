#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:lqx


import requests
from bs4 import BeautifulSoup
response_acc=requests.get(
    url='https://github.com/login',
)
response_acc.encoding=response_acc.apparent_encoding
cookie=response_acc.cookies.get_dict()
# print(response.text)

soup=BeautifulSoup(response_acc.text,'html.parser')
token=soup.find(name='input',attrs={'name':'authenticity_token'}).get('value')
print(token)

response_login=requests.post(
    url='https://github.com/session',
    data={
        'commit': 'Sign in',
        'utf8': '✓',
        'authenticity_token': token,
        'login': '18311166263@163.com',
        'password': 'liu890892'
    },
    allow_redirects=True,
    cookies=cookie
)
# print(response_login.text)
# print(response_login.url)

soup_login=BeautifulSoup(response_login.text,'html.parser')
ul=soup_login.find_all(name='ul',attrs={'class':'dropdown-menu dropdown-menu-sw'})[1]
# print(ul)
hrefs=ul.find_all(attrs={'class':'dropdown-item'})
# print(hrefs)
for i in hrefs:
    href=i.get('href',)
    href_text=i.get_text()
    # print(href,href_text)
    if 'profile' in href_text:
        response_profile=requests.get(
            url='%s%s'%(response_login.url,href)

        )
        response_reposit=requests.get(
            url='%s/six-lqx?tab=repositories'%(response_login.url)
        )
        soup_pro=BeautifulSoup(response_reposit.text,'html.parser')
        div=soup_pro.find_all(attrs={'class':'d-inline-block mb-1'})
        for i in div:
            for o in i.find_all(name='a'):
                print(o.get('href'))




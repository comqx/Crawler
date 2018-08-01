#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:lqx
import requests

#ajax提交数据模拟登陆

#一定要一步一步的伪造浏览器的行为
#1、访问网页得到未授权的cookies (未授权的cookie)
response_int=requests.get(
    url='https://dig.chouti.com/',
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    }

)
# print(response_int.text)
r1_cookie_dict=response_int.cookies.get_dict()
# print(response_int.cookies.get_dict())

#2、发送用户名密码认证+cookie(未授权)
#发送post请求
#注意防爬虫策略：请求头会携带信息
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
print(response_login.text)
#返回cookies
# cookies_login=response_login.cookies.get_dict()
# print(response_login.cookies.get_dict())


# 点赞功能实现：
response=requests.post(
    url='https://dig.chouti.com/link/vote?linksId=20156701',
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'
    },
    cookies=r1_cookie_dict
)
print(response.text)





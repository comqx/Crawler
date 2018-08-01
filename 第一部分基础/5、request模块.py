#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:lqx

import requests

requests.get(url='x')  #requests.request(method='get',url='x')
requests.post(url='x')  #requests.request(method='post',url='x')

requests.get(
    url='x',
    #get在url中传参，使用params
    params={
        'nid':1,
        'name':'name',
            },
    headers={},
    cookies={},
)



requests.post(
    url='x',
    data={},
    headers={},
    cookies={}
)


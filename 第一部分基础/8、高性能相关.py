#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:lqx
import requests
# from concurrent.futures import ThreadPoolExecutor
from threading import Thread
url_list=[
    'http://jandan.net/duan',
    'http://jandan.net/pic',
    'http://jandan.net/',

]
def task(url):
    ret=requests.get(url)
    print(ret)
#
# pool=ThreadPoolExecutor(10)
#
# for url in url_list:
#     pool.

for url in url_list:
    t=Thread(target=task,args=(url,))
    t.start()

#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:lqx
import socket
def task(url='www.cnblogs.com'):
    sk=socket.socket()
    #阻塞：连接的过程
    sk.connect((url,80))

    #http协议
    content='GET /lqx HTTP/1.1\r\nHost:%s\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36\r\n\r\n'%url
    sk.sendall(content.encode('utf-8'))
    #阻塞：等待服务器返回内容
    data=sk.recv(8096)
    print(data.decode('utf-8'))
    sk.close()

url_list=[
    'www.baidu.com',
    'www.cnblogs.com',
    'www.jandan.com',
]
for url in url_list:
    task(url)

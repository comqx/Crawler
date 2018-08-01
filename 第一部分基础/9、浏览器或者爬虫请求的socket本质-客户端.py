#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:lqx

#向这个地址发送GET请求：http://www.cnblogs.com/lqx

import socket

sk=socket.socket()
#阻塞：连接的过程
sk.connect(('www.cnblogs.com',80))

#http协议
sk.sendall(b'GET /lqx HTTP/1.1\r\nHost:www.cnblogs.com\r\nConnection: keep-alive\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36\r\n\r\n ')

#阻塞：等待服务器返回内容
data=sk.recv(8096)
print(data.decode('utf-8'))
sk.close()

#本质上就等价于下面的requests
import requests
ret=requests.get('http://www.cnblogs.com/lqx')
#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:lqx
import socket

sk=socket.socket()
sk.bind(('127.0.0.1',8001))
sk.listen(5)

while True:
    #阻塞，等待用户来连接
    client,addr=sk.accept()

    #阻塞，等待用户发送数据过来
    req=client.recv(8096)
    print(req)
    client.sendall(b'xxxxx')
    client.close()



sk.connect(('www.cnblogs.com',80,))
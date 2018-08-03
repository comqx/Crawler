#!/usr/bin/env python
#-*- coding: utf-8 -*-
# writer:lqx

import socket,select

class AsyncHttp(object):
    def __init__(self):
        self.fds=[]
        self.conn=[]

    def add(self,url):
        sk=socket.socket()
        sk.setblocking(False)  #socket发生数据不阻塞
        try:
            sk.connect((url,80))
        except BlockingIOError as e:
            pass
        self.fds.append(sk)
        self.conn.append(sk)

    def run(self):
        '''
        监听socket是否发生变化
        :return:
        '''
        while True:
            '''
            fds=[sk1,sk2,sk3]
            conn=[sk1,sk2,sk3]
            '''
            r,w,e=select.select(self.fds,self.conn,[],0.05)
            # print(len(w))
            #w=已经连接成功的socket列表w=[sk1,sk2]
            for client in w:
                client.sendall(b'GET /lqx HTTP/1.1\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36\r\n\r\n ')
                self.conn.remove(client) #已经连接成功的socket，无需再监听
            #r=已经收到数据的socket列表r=[sk1,sk2]
            for cli in r:
                date=cli.recv(8096)
                print('数据获取到')
                #断开连接，短连接、无状态
                cli.close() #不再监听
                self.fds.remove(cli)
            if not self.fds: break

ah=AsyncHttp()

ah.add('www.cnblogs.com')
ah.add('www.luffycity.com')
ah.add('www.baidu.com')

ah.run()
#!/usr/bin/env python
#coding:utf-8
from socket import *
from time import ctime
HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)
#创建服务费套接字
tcpSerSock = socket()
#将地址绑定到套接字上
tcpSerSock.bind(ADDR)
#设置并启动TCP监听器
tcpSerSock.listen(5)
while True:
    print '------waiting for connection------'
    #被动接受TCP客户端连接直到连接到达（阻塞）
    tcpCliSock,addr = tcpSerSock.accept()
    print '------connected from :' ,addr
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(('[%s] %s') % (ctime(),data))
    tcpCliSock.close()
tcpSerSock.close()
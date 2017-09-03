#!/usr/bin/env python
#coding:utf-8
from socket import *
HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024
ADDR = (HOST,PORT)
#创建客户端套接字
tcpCliSock = socket()
tcpCliSock.connect(ADDR)
while True:
    data = raw_input('Please input your message:')
    if not data:
        break
    tcpCliSock.send(data)
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print data
tcpCliSock.close()
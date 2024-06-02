#!/usr/bin/python

import sys
from socket import *
#sys.setdefaultencoding('utf-8')
serverName = '127.0.0.1'

serverPort = int(sys.argv[1])

clientSocket = socket(AF_INET , SOCK_STREAM)

clientSocket.connect((serverName , serverPort))

sentence = input('Input lowercase sentence')

print('sentence is ' + sentence)
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From server: ' , modifiedSentence.decode())
clientSocket.close()


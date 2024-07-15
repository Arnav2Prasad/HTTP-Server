#!usr/bin/python

import sys
from socket import *

serverName = '10.1.149.200'
#connectionSocket, addr = serverSocket.accept()
serverPort = 12005
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, int(serverPort)))

message=''
message += "OPTIONS / HTTP/1.1\r\n"
# message += 'connection : keep-alive\r\n'
message += "Host        :127.0.0.1:80\r\n"
# message += "If-unmodified-since : Sun, 11 May 2024 06:20:37 GMT\r\n"
#message += "Accept: text/html\r\n"
# message += "Accept-Charset: UTF-8\r\n"
# message += "If-modified-since : Sun, 22 Jun 2024 06:20:37 GMT\r\n"
# message += "If-Modified-Since : Sun, 23 Jun 2024 06:21:33 GMT\r\n"
message += "\r\n"

print("message to be sent : ", message)
# while True:
clientSocket.send(message.encode())

modifiedSentence = (clientSocket.recv(1024))
print("message from server is : \n", modifiedSentence.decode(), sep='')
clientSocket.close()

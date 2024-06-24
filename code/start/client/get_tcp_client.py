#!usr/bin/python

import sys
from socket import *

serverName = '127.0.0.1'
#connectionSocket, addr = serverSocket.accept()
serverPort = 12005
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, int(serverPort)))

message=''
message += "GET /home/arjun/httpfiles/2.html HTTP/1.1\r\n"
#message += "Host            :   127.0.0.1:80\r\n"
message += "\r\n"

print("message to be sent : ", message)
clientSocket.send(message.encode())
modifiedSentence = (clientSocket.recv(1024))
print("message from server is : \n", modifiedSentence.decode())
clientSocket.close()

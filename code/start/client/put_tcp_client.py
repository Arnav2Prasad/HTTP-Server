#!usr/bin/python

import sys
from socket import *

serverName = '127.0.0.1'
#connectionSocket, addr = serverSocket.accept()
serverPort = sys.argv[1]
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, int(serverPort)))

message=''
message += "PUT /home/arjun/httpfiles/3 HTTP/1.1\r\n"
message += "Host            :   127.0.0.1\r\n"
message += "\r\n"
message += "voih epi eo iej  fuef ;; gsusy 1 !"

print("message to be sent : ", message)
clientSocket.send(message.encode())
modifiedSentence = (clientSocket.recv(1024))
print("message from server is : \n", modifiedSentence.decode())
clientSocket.close()

#!usr/bin/python

import sys
from socket import *

serverName = '10.1.149.200'
#connectionSocket, addr = serverSocket.accept()
# serverPort = sys.argv[1]
serverPort = 12005
clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName, int(serverPort)))

message=''
message += "PUT /home/arnav/httpfiles/6 HTTP/1.1\r\n"
message += "Host            :   127.0.0.1\r\n"
message += "\r\n"
message += "\"[asdtfiuastdf]\""

print("message to be sent : ", message)
clientSocket.send(message.encode())
modifiedSentence = (clientSocket.recv(1024))
print("message from server is : \n", modifiedSentence.decode())
clientSocket.close()

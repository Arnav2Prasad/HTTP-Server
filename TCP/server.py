#!/usr/bin/python

from socket import *

#socket is a "service-endpoint". Socket serves networking code, bus also non-networking code.
#AF_INET tells that its IPv4 networking socket.
serverSocket = socket(AF_INET , SOCK_STREAM)

#The server opens a socket, but must "bind" it to a name - called port.
serverPort = 12000

serverSocket.bind(('127.0.0.1',serverPort));

#after that server listens , waits for someone to send a connection request.
# this is not in UDP
serverSocket.listen(1)

print('the server is ready to recieve')

while True:
    #will block untill someone connects
    #new connection will get created each time ie connectionSocket
    connectionSocket , addr = serverSocket.accept()
    print('new request recieved from');print(addr);
    print('connectionSocket is');print(connectionSocket);
    sentence = connectionSocket.recv(1024).decode()
    cpaitalizedSentence = sentence.upper()
    connectionSocket.send(cpaitalizedSentence.encode())
    connectionSocket.close()

#I want to send a letter to you. But you never want to start a communication with me.
#I am the client and you are a server.
#Your and my house may have 100 doors, but at least one door in your house, must be known to me.


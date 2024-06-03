#!/usr/bin/python

import sys
from socket import *

serverPort = int(sys.argv[1])
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('127.0.0.1', serverPort))
message = "GET /index.html HTTP/1.1\r\n"
message += "HOST:moodle.coep.org.in\r\n"
message += "\r\n"
x = clientSocket.send(message.encode())
while True:
    data = clientSocket.recv(4096).decode()
    print(data)

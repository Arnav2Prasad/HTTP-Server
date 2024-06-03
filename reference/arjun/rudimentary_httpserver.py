#!/usr/bin/python
# this is NOT how the project code is to be written
# for study purpose only
# this code takes actions based on the request lines
# this is just to test the format, other stuff

import sys
import string as str
from socket import *

# this is the path where files are stored
# this should ideally be in some other file
serverPath = '/home/arjun/serverfiles'

# serverPort is the 1st command line argument
serverPort = int(sys.argv[1])

# server socket created
serverSocket = socket(AF_INET, SOCK_STREAM)

# bind the socket
serverSocket.bind(('', serverPort))

# listen on the socket
serverSocket.listen(1)

# this function decodes the request line of HTTP message, and takes actions
def decode_req_line(req_line_str):
    # tokenise the line
    tokens = req_line_str.split(sep=' ')
    print("tokens are : ", tokens)

    # GET method
    # for now, just the requested file is returned without
    # checking the header details
    # THIS IS NOT HOW IT IS TO BE DONE IN THE PROJECT
    if tokens[0] == 'GET':
        connectionSocket.send("GET method".encode())
        file_path = serverPath + tokens[1]
        print("filePath is ", file_path)

        # open file with specified path as 
        # serverPath concatenated with requested object path
        file = open(file_path, 'r')

        # read contents of file into buffer
        file_contents = file.read()

        # send them into the socket
        connectionSocket.send(file_contents.encode())


print("the server is ready to recieve")

while True:
    connectionSocket, addr = serverSocket.accept()
    print("message recieved from : ", addr)
    sentence = connectionSocket.recv(4096).decode()
    print(sentence)
    tokens = sentence.splitlines()
    print("tokens found : ", tokens)
    decode_req_line(tokens[0])


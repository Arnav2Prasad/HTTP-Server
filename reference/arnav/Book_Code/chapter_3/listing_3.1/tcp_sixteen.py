
#!/usr/bin/env python3
# Simple TCP client and server that send and receive 16 octets
import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = sys.argv.pop() if len(sys.argv) == 3 else '127.0.0.1'
PORT = 1060

def recv_all(sock, length):
    data = b''
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('socket closed %d bytes into a %d-byte message'
                           % (len(data), length))
        data += more
    return data

if sys.argv[1:] == ['server']:
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    while True:
	#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Listening at', s.getsockname())
        sc, sockname = s.accept()
        print('We have accepted a connection from', sockname)
        print('Socket connects', sc.getsockname(), 'and', sc.getpeername())
        message = recv_all(sc, 16)
        print('The incoming sixteen-octet message says', repr(message))
        sc.sendall(b'Farewell, client')
        sc.close()
        print('Reply sent, socket closed')
elif sys.argv[1:] == ['client']:
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    print('Client has been assigned socket name', s.getsockname())
    s.sendall(b'Hi there, server')
    reply = recv_all(s, 16)
    print('The server said', repr(reply))
    s.close()
else:
    print('usage: tcp_local.py server|client', file=sys.stderr)

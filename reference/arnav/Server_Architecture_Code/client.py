
#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 7 - client.py
# Simple Lancelot client that asks three questions then disconnects.

import socket, sys, launcelot

def client(hostname, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((hostname, port))
    s.sendall(launcelot.qa[0][0])
    answer1 = launcelot.recv_until(s, b'.')  # answers end with '.'
    s.sendall(launcelot.qa[1][0])
    answer2 = launcelot.recv_until(s, b'.')
    s.sendall(launcelot.qa[2][0])
    answer3 = launcelot.recv_until(s, b'.')
    s.close()
    print(answer1)
    print(answer2)
    print(answer3)

if __name__ == '__main__':
    if not 2 <= len(sys.argv) <= 3:
        print('usage: client.py hostname [port]', file=sys.stderr)
        sys.exit(2)
    port = int(sys.argv[2]) if len(sys.argv) > 2 else launcelot.PORT
    client(sys.argv[1], port)

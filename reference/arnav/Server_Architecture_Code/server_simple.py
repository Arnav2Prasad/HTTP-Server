
#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 7 - server_simple.py
# Simple server that only serves one client at a time; others have to wait.

import launcelot

def handle_client(client_sock):
    try:
        while True:
            question = launcelot.recv_until(client_sock, b'?')
            answer = launcelot.qadict[question]
            client_sock.sendall(answer)
    except EOFError:
        client_sock.close()

def server_loop(listen_sock):
    while True:
        client_sock, sockname = listen_sock.accept()
        handle_client(client_sock)

if __name__ == '__main__':
    listen_sock = launcelot.setup()
    server_loop(listen_sock)

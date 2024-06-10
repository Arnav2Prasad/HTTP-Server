
#!/usr/bin/env python
# Foundations of Python Network Programming - Chapter 2 - udp_local.py
# UDP client and server on localhost

import socket
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
MAX = 65535
PORT = 1060

if sys.argv[1:] == ['server']:
    s.bind(('127.0.0.1', PORT))
    print('Listening at', s.getsockname())
    while True:
        data, address = s.recvfrom(MAX)
        print('The client at', address, 'says', repr(data))
        s.sendto(b'Your data was %d bytes' % len(data), address)
elif sys.argv[1:] == ['client']:
    print('Address before sending:', s.getsockname())
    s.sendto(b'This is my message', ('127.0.0.1', PORT))
    print('Address after sending', s.getsockname())
    data, address = s.recvfrom(MAX)  # overly promiscuous - see text!
    print('The server', address, 'says', repr(data))
else:
    print('usage: udp_local.py server|client', file=sys.stderr)

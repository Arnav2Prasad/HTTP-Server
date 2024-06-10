Python 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> import socket
>>> socket.getservbyname('domain')
53
>>> socket.getservbyname('http')
80
>>> socket.getservbyname('https')
443
>>> socket.getservbyname('ftp')
21
>>> socket.getservbyname('smtp')
25
>>> socket.getservbyname('pop3')
110
>>> socket.getservbyname('imap')
143
>>> socket.getservbyname('telnet')
23
>>> socket.getservbyname('ssh')
22
>>> socket.getservbyname('nntp')
119

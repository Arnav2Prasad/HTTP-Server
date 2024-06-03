# UDP client AND server on localhost

import socket, sys

# allocates a socket to s, which is a UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# maximum size of data (int bytes) to be sent through a socket
MAX = 65535

# server port to be used
SER_PORT = 12000

# if command line argument says 'server'
if sys.argv[1] == 'server':

    # bind it to a socket
    s.bind(('127.0.0.1', SER_PORT))
    print('listening at', s.getsockname())

    # keep recieving data from the bound socket
    while True:
        # recvfrom() returns a pair, containing data as well as address
        data, address = s.recvfrom(MAX)
        print('the client at ', address, 'sent ', data.decode())
        message = ' Your message was '+ str(len(data.decode())) +  ' bytes long'
        message += ', thank you for sending ' + '\'' +  data.decode() + '\''

        # send the data back to from where it was recieved
        s.sendto(message.encode(), address)

# if command line argument says 'client'
elif sys.argv[1] == 'client':

    # initially, socket s had address = ('0.0.0.0', 0)
    print('Address before sending : ', s.getsockname())
    message = 'hello world' 
    s.sendto(message.encode(), ('127.0.0.1', SER_PORT))

    # after the sendto() function is called, rather during it
    # OS allocates a random port number to socket s
    print('Address after sending : ', s.getsockname())

    # just like server, recieve data from the socket
    data, address = s.recvfrom(MAX)
    print(data)
    print('The server', address, 'says ', data.decode())

else:
    print >> sys.stderr, 'usage: udp_ser_cli.py server|client port'

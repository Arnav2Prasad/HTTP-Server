#!/usr/bin/env python3
# Foundations of Python Network Programming - Chapter 2 - big_sender.py
# Send a big UDP packet to our server.

import socket
import sys
import IN

# Initialize UDP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define constants
MAX = 65535
PORT = 1060

# Validate command-line arguments
if len(sys.argv) != 2:
    print('usage: big_sender.py host', file=sys.stderr)
    sys.exit(2)

# Extract hostname from command-line arguments
hostname = sys.argv[1]

# Connect to the specified host and port
s.connect((hostname, PORT))

# Enable Path MTU Discovery (PMTUD)
s.setsockopt(socket.IPPROTO_IP, IN.IP_MTU_DISCOVER, IN.IP_PMTUDISC_DO)

# Try sending a big packet
try:
    s.send(b'#' * 65000)
except socket.error:
    print('The message did not make it', file=sys.stderr)
    option = getattr(IN, 'IP_MTU', 14)  # constant taken from <linux/in.h>
    print('MTU:', s.getsockopt(socket.IPPROTO_IP, option))
else:
    print('The big message was sent! Your network supports really big packets!')

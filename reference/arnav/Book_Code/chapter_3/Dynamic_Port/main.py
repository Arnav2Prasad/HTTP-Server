Sure! To create a server that dynamically assigns a new port for each client, you would typically need to handle the connection 
acceptance in such a way that each client communicates through a new port. This can be done by creating a new socket bound to a 
new port for each client connection. 

Here's an example that demonstrates how to achieve this:

# Server Code

import socket
import threading

def handle_client(client_socket, client_address):
    print(f"Handling client {client_address}")

    # Receive the message
    message = client_socket.recv(16)
    print(f"Received message from {client_address}: {message}")

    # Send a reply
    client_socket.sendall(b"Reply from server")
    
    # Close the connection
    client_socket.close()
    print(f"Connection with {client_address} closed")

def main():
    # Create a socket object for the initial listening socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind(('127.0.0.1', 1060))
    server_socket.listen(5)
    print("Server listening on port 1060")

    while True:
        # Accept a new connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Create a new socket for communication with the client
        new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        new_socket.bind(('127.0.0.1', 0))  # Bind to any available port
        new_socket.listen(1)

        # Get the dynamically assigned port number
        new_port = new_socket.getsockname()[1]
        print(f"New port for {client_address} is {new_port}")

        # Send the new port number to the client
        client_socket.sendall(f"{new_port}".encode())
        client_socket.close()

        # Accept connection on the new socket
        conn, addr = new_socket.accept()
        print(f"New connection accepted from {addr} on port {new_port}")

        # Handle the client connection in a new thread
        client_handler = threading.Thread(target=handle_client, args=(conn, addr))
        client_handler.start()

if __name__ == "__main__":
    main()
```

# Client Code

```python
import socket

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server on the initial port
    client_socket.connect(('127.0.0.1', 1060))

    # Receive the new port number
    new_port = int(client_socket.recv(16).decode())
    print(f"New port received: {new_port}")

    # Close the initial connection
    client_socket.close()

    # Create a new socket for the new connection
    new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server on the new port
    new_socket.connect(('127.0.0.1', new_port))

    # Send a message to the server
    new_socket.sendall(b"Hi there, server")

    # Receive the server's reply
    reply = new_socket.recv(16)
    print(f"Received reply: {reply}")

    # Close the connection
    new_socket.close()

if __name__ == "__main__":
    main()

--------------------------------------
#Explanation

1. Server Side:
   - The server initially listens on port 1060.
   - When a client connects, the server accepts the connection, creates a new socket, binds it to an available port, 
       and starts listening on that port.
   - The server sends the new port number to the client and closes the initial connection.
   - The server then accepts a connection on the new port and handles the client communication in a separate thread.

2. Client Side:
   - The client connects to the server on port 1060 to initiate the communication.
   - The client receives the new port number from the server, closes the initial connection, and then connects 
       to the server on the new port.
   - The client sends a message and receives a reply on the new connection.

This setup ensures that each client communicates with the server through a different dynamically 
assigned port after the initial connection setup.




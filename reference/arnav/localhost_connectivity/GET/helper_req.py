

import socket

def recv_all(sock, length):
    data = b''  # Use a bytes object instead of a string
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('socket closed %d bytes into a %d-byte message' % (len(data), length))
        data += more
    return data

def run_server(host='127.0.0.1', port=1060):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Listening at {host, port}")

        while True:
            client_connection, client_address = server_socket.accept()
            print(f"Connection came from {client_address[0]}:{client_address[1]}")
            with client_connection:
                try:
                    message = recv_all(client_connection, 16)
                    print(f"Received message: {message}")
                    response = b'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!'
                    client_connection.sendall(response)
                except EOFError as e:
                    print(e)

if __name__ == "__main__":
    run_server()



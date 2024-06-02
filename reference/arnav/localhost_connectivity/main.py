
import socket

def handle_request(request):
    # A simple HTTP response
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        "\r\n"
        "<html><body><h1>Hello, World!</h1></body></html>"
    )
    print("request is : ")
    print(request)
    return response.encode('utf-8')

def run_server(host='127.0.0.1', port=1070):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Listening at {host, port}")

        while True:
            client_connection, client_address = server_socket.accept()
            print("client_connection : " , client_connection)
            print("client_address : " , client_address)
            print('--------------------------------------')
            print(f"Connection came from {client_address[0]}:{client_address[1]}")
            with client_connection:
                request = client_connection.recv(1024)
                if not request:
                    break
                response = handle_request(request)
                client_connection.sendall(response)
    print('--------------------------------------')
    print('--------------------------------------')
    print('--------------------------------------')

if __name__ == "__main__":
    run_server()


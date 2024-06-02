
import socket

def handle_request(request):
    request_lines = request.decode('utf-8').split('\r\n')
    request_line = request_lines[0]
    headers = {}

    for line in request_lines[1:]:
        if line == '':
            break
        header, value = line.split(': ', 1)
        headers[header] = value

    if 'Content-Length' in headers:
        body_start = request.index(b'\r\n\r\n') + 4
        body = request[body_start:body_start + int(headers['Content-Length'])].decode('utf-8')
    else:
        body = ''

    if request_line.startswith('POST'):
        response_body = (
            f"<html><body><h1>Received POST Request</h1>"
            f"<p>Request Body: {body}</p></body></html>"
        )
    else:
        response_body = "<html><body><h1>Hello, World!</h1></body></html>"

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(response_body)}\r\n"
        "\r\n"
        f"{response_body}"
    )
    print("Request:")
    print(request.decode('utf-8'))
    print("Body:")
    print(body)
    return response.encode('utf-8')

def run_server(host='127.0.0.1', port=1070):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Listening at {host, port}")

        while True:
            client_connection, client_address = server_socket.accept()
            print(f"Connection from {client_address[0]}:{client_address[1]}")
            with client_connection:
                request = client_connection.recv(1024)
                if not request:
                    break
                response = handle_request(request)
                client_connection.sendall(response)

if __name__ == "__main__":
    run_server()


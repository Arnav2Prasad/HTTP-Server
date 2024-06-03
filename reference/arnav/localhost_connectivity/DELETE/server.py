
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
    elif request_line.startswith('PUT'):
        response_body = (
            f"<html><body><h1>Received PUT Request</h1>"
            f"<p>Request Body: {body}</p></body></html>"
        )
    elif request_line.startswith('DELETE'):
        response_body = (
            f"<html><body><h1>Received DELETE Request</h1>"
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

# Setting up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 1080))
server_socket.listen(1)
print('Server is running on port 1080...')

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Connection from {client_address}')
    request = client_socket.recv(1024)
    response = handle_request(request)
    client_socket.sendall(response)
    client_socket.close()


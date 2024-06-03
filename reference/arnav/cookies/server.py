import socket

'''
parse_cookies takes a cookie_header string and parses it into a dictionary of cookies.
It splits the header on ; to separate individual cookies.
Each cookie is then split on = to get the key and value, which are stored in a dictionary.
'''
def parse_cookies(cookie_header):
    cookies = {}
    if cookie_header:
        for cookie in cookie_header.split('; '):
            key, value = cookie.split('=', 1)
            cookies[key] = value
    return cookies

def handle_request(request):
    request_lines = request.decode('utf-8').split('\r\n')
    request_line = request_lines[0]
    headers = {}
    cookies = {}

    for line in request_lines[1:]:
        if line == '':
            break
        header, value = line.split(': ', 1)
        headers[header] = value
        if header == 'Cookie':
            cookies = parse_cookies(value)

    if 'Content-Length' in headers:
        body_start = request.index(b'\r\n\r\n') + 4
        body = request[body_start:body_start + int(headers['Content-Length'])].decode('utf-8')
    else:
        body = ''

    '''
    Checks if the request_count cookie is present.
    If present, it increments the count; otherwise, it initializes the count to 1.
    '''
    # Retrieve the request count from the cookies and update it
    if 'request_count' in cookies:
        request_count = int(cookies['request_count']) + 1
    else:
        request_count = 1

    if request_line.startswith('POST'):
        response_body = (
            f"<html><body><h1>Received POST Request</h1>"
            f"<p>Request Body: {body}</p>"
            f"<p>Request Count: {request_count}</p></body></html>"
        )
    elif request_line.startswith('PUT'):
        response_body = (
            f"<html><body><h1>Received PUT Request</h1>"
            f"<p>Request Body: {body}</p>"
            f"<p>Request Count: {request_count}</p></body></html>"
        )
    elif request_line.startswith('DELETE'):
        response_body = (
            f"<html><body><h1>Received DELETE Request</h1>"
            f"<p>Request Body: {body}</p>"
            f"<p>Request Count: {request_count}</p></body></html>"
        )
    elif request_line.startswith('HEAD'):
        response_body = ""  # No body for HEAD request
    else:
        response_body = (
            f"<html><body><h1>Hello, World!</h1>"
            f"<p>Request Count: {request_count}</p></body></html>"
        )

    # Set the updated request count in the response cookie
    response_headers = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(response_body)}\r\n"
        f"Set-Cookie: request_count={request_count}; Path=/; HttpOnly\r\n"
        "\r\n"
    )

    response = response_headers + response_body
    print("Request:")
    print(request.decode('utf-8'))
    print("Body:")
    print(body)
    print("Cookies:")
    print(cookies)
    print('------------------------')
    print('Response :')
    print(response)
    print('-------------------------')
    return response.encode('utf-8')

# Setting up the server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 1090))

# Listens for incoming connections, with a backlog of 1 connection.
server_socket.listen(1)
print('Server is running on port 1090...')

'''
Enters an infinite loop to handle incoming connections.
Accepts a connection, which returns a new socket for communication and the client's address.
Receives up to 1024 bytes from the client.
Processes the request using handle_request to generate a response.
Sends the response back to the client.
Closes the connection.
'''

while True:
    client_socket, client_address = server_socket.accept()
    print(f'Connection from {client_address}')
    request = client_socket.recv(1024)
    response = handle_request(request)
    client_socket.sendall(response)
    client_socket.close()


'''
Summary

    This server processes HTTP requests and maintains a count of requests per client using cookies.
    It handles various HTTP methods and sets the request_count cookie to track the number of requests.
    The server responds with HTML that includes the current request count.
    It runs indefinitely, handling one connection at a time.
'''

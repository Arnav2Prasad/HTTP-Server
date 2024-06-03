
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

    '''
    Checks if the 'Content-Length' header is present in the headers dictionary.
    If present, calculates the start position of the body by finding the index of 
    the double CRLF (\r\n\r\n), which separates headers from the body, and adds 4 to 
    move past the CRLF itself.
    
    Extracts the body by slicing the request from the calculated start position to the length 
    specified by 'Content-Length', and decodes it from UTF-8 to a string.
    
    If 'Content-Length' is not present, sets the body to an empty string.
    '''
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
    
    
'''
Question : Does the http response that the server sends, includes the body of the "request" 
        it get from the client?
        
EXPLANATION :
    Yes, that's correct. 
    The HTTP response that the server sends back to the client includes the body of the request 
    it received from the client.
    
    --> If the request has a Content-Length header, the server extracts the body of the 
        request from the raw request data.
    
    --> If the request is a POST request, the server generates an HTML response that includes 
        the body of the request it received.
        
        
    Constructing the HTTP Response:

    The server constructs the HTTP response as follows:

    Create Response Body:
        The response body is a string of HTML that includes the request body.

        response_body = (
            f"<html><body><h1>Received POST Request</h1>"
            f"<p>Request Body: {body}</p></body></html>"
        )

    Create Complete HTTP Response:
        The response includes the status line, headers, and the response body.

    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {len(response_body)}\r\n"
        "\r\n"
        f"{response_body}"
    )

    Example Workflow


    Client Sends POST Request:
        The client sends a POST request to the server, including some data in the body.

        POST /your-endpoint HTTP/1.1
        Host: localhost:1080
        Content-Type: application/x-www-form-urlencoded
        Content-Length: 27

        name=John+Doe&email=john%40example.com

    
    Server Processes Request:
        The server extracts the body (name=John+Doe&email=john%40example.com) from the request and 
        constructs an HTML response that includes this body.


    Server Sends Response:
        The server sends back an HTTP response that includes the extracted request body in the HTML content.

        HTTP/1.1 200 OK
        Content-Type: text/html; charset=utf-8
        Content-Length: 102

        <html><body><h1>Received POST Request</h1><p>Request Body: name=John+Doe&email=john%40example.com</p></body></html>

    
    
    SUMMARY
    The server receives an HTTP request and extracts the body if it has a Content-Length header.
    Based on the request method (POST or PUT), the server constructs an HTML response that includes 
    the body of the request it received.
    The server sends this response back to the client, so the client can see the data 
    it sent reflected in the server's response.

            This approach helps in debugging and verifying that the server correctly 
            receives and processes the data sent by the client.
'''



import socket

'''
This defines a function named handle_request that takes one parameter, request, 
which represents the raw HTTP request data received by the server.
'''
def handle_request(request):
    '''
    This line decodes the raw byte data (request) from UTF-8 to a string, then splits 
    the string into a list of lines using the carriage return and line feed (\r\n) as the 
    delimiter. request_lines now contains each line of the HTTP request as a separate string.
    '''
    request_lines = request.decode('utf-8').split('\r\n')
    
    '''
    This extracts the first line of the request, known as the request line, 
    which contains the HTTP method (e.g., GET, POST), the request URI, and the HTTP version.
    '''
    request_line = request_lines[0]
    headers = {}

    '''
    This loop iterates over each line in request_lines starting from the second line (index 1). 
    It stops when it encounters an empty line, which indicates the end of the headers section.
    Each line is split into a header name (header) and its corresponding value (value) at the first 
    occurrence of ': '. These key-value pairs are added to the headers dictionary.
    '''
    for line in request_lines[1:]:
        if line == '':
            break
        header, value = line.split(': ', 1)
        headers[header] = value
    
    '''
    Checks if the 'Content-Length' header is present in the headers dictionary.
    If present, it calculates the start position of the body by finding the index of the 
    double CRLF (\r\n\r\n), which separates headers from the body, and adds 4 to 
    move past the CRLF itself.
    It then extracts the body by slicing the request from the calculated start position to the 
    length specified by 'Content-Length', and decodes it from UTF-8 to a string.
    If 'Content-Length' is not present, it sets the body to an empty string.
    '''

    if 'Content-Length' in headers:
        body_start = request.index(b'\r\n\r\n') + 4
        body = request[body_start:body_start + int(headers['Content-Length'])].decode('utf-8')
    else:
        body = ''
        
    '''
    Checks if the request method in request_line starts with 'POST'.    
    If it is a POST request, it constructs an HTML response body containing a message and the 
    contents of the request body.
    If it is not a POST request, it constructs a simpler HTML response body with a "Hello, World!" message. 
    '''
    if request_line.startswith('POST'):
        response_body = (
            f"<html><body><h1>Received POST Request</h1>"
            f"<p>Request Body: {body}</p></body></html>"
        )
    else:
        response_body = "<html><body><h1>Hello, World!</h1></body></html>"

    '''
    Constructs the HTTP response. The response consists of:

        (i) The status line (HTTP/1.1 200 OK) indicating a successful request.
        (ii) The Content-Type header specifying the type and encoding of the response 
        (text/html; charset=utf-8).
        (iii) The Content-Length header indicating the length of the response body.
        (iv) A blank line (\r\n) to separate headers from the body.
        (v) The actual HTML response body.
    '''
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


'''
This function is defined to run a server. It takes two optional arguments: host, 
which defaults to '127.0.0.1' (localhost), and port, which defaults to 1070.
'''
def run_server(host='127.0.0.1', port=1070):
    '''
    This line creates a socket object using the socket module. 
    It uses the AF_INET address family, which is used for IPv4 addresses, and 
    the SOCK_STREAM type, which indicates a TCP socket. The with statement ensures 
    that the socket is properly closed after use.
    '''
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        '''
        These lines bind the socket to the specified host and port and start listening for 
        incoming connections. server_socket.listen(1) sets the maximum number of queued connections to 1, 
        meaning that if there's already one connection being handled, new connections will be queued.
        '''
        server_socket.bind((host, port))
        server_socket.listen(1)
        print(f"Listening at {host, port}")

        while True:
            '''
            This line blocks until a client connects to the server. Upon connection, it returns a 
            new socket object representing the connection (client_connection) and the address of 
            the client (client_address).
            '''
            client_connection, client_address = server_socket.accept()
            print(f"Connection from {client_address[0]}:{client_address[1]}")
            '''
            Inside a with block, the server receives data from the client with client_connection.recv(1024), 
            which reads up to 1024 bytes of data. If no data is received (indicating the client closed the 
            connection), the loop breaks. Otherwise, it calls a function handle_request() to process the 
            request and sends back the response to the client with client_connection.sendall(response).
            '''
            with client_connection:
                request = client_connection.recv(1024)
                # explained below
                if not request:
                    break
                
                response = handle_request(request)
                client_connection.sendall(response)

if __name__ == "__main__":
    run_server()
    
    
'''
The line `if not request: break` is checking whether the received data is empty. 
If the received data is empty, it generally indicates that the client has closed the connection. 
However, it's important to understand that this behavior might not necessarily mean the message is delayed.

In a TCP connection, data is transmitted in packets, and delays can occur due to network congestion, 
server load, or other factors. However, even if there's a delay in the message reaching the server, 
as long as the connection remains open, the server will eventually receive the message. 
The delay in transmission doesn't make the received data empty.

The condition `if not request` is primarily checking for the case where the client 
has closed the connection, which is a common scenario to handle in server applications. 
However, if the delay is due to network congestion or other factors, the condition wouldn't 
trigger just because of the delay. It triggers only when there's truly no data being received, 
such as when the client has ended the connection.
'''


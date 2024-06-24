
from headers.host import *

from delete import *
from get import *
from put import *
from common import *


http_status_codes = {
    100: "Continue",
    101: "Switching Protocols",
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non-Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    307: "Temporary Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Request Entity Too Large",
    414: "Request-URI Too Long",
    415: "Unsupported Media Type",
    416: "Requested Range Not Satisfiable",
    417: "Expectation Failed",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported"
}



serverPort = 12005
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

serverSocket.bind(('', serverPort))
serverSocket.listen(10)

print("the server is ready to recieve")

def get_dict_from_header(req):
    print(req)
    print('wwwwwwwwwwwwwwwwwwwwwwww')
    request_lines = req.split('\r\n')
    header_body = ''
    
    print("ppppppppppppppppp")
    print(request_lines)
    length = len(request_lines)
    print('length : ' , length)
    dict={}
    start_line = request_lines[0]
    y=length
    for i in range(1,length):
        req_each_line = request_lines[i]
        if req_each_line=='':
            y=i
            # print('hehehehe')
            break
        print(req_each_line)
        header_key = ''
        i=0
        for ch in req_each_line:
            if ch==':':
                break
            header_key += ch
            i=i+1
        header_key = header_key.strip()
        header_key = header_key.lower()
        # print(header_key)
        
        
        print(i)
        header_message = req_each_line[i+2:].strip()
        print(header_key)
        print(header_message)
        print('---------------')
        dict[header_key] = header_message
    for k in range(y,length):
            if header_body == '':
                header_body += request_lines[k]
            else:
                header_body += '\r\n' + request_lines[k]
        
    # if 'Content-Length' in dict:
    #     body_start = .index(b'\r\n\r\n') + 4
    #     body = request[body_start:body_start + int(headers['Content-Length'])].decode('utf-8')
    # else:
    #     body = ''

    tp_response = (
            f"<html><body><h1>Received POST Request</h1>"
            f"<p>Request Body: {'hii, this is Arnav!'}</p></body></html>"
        )
    return start_line,dict,header_body
 
def doIO_socket(connectionSocket):
    print("connection made in thread : ", connectionSocket)
    sentence = connectionSocket.recv(1024).decode()
    while sentence:
        response = process_request(sentence)

        connectionSocket.send(response.encode())
        sentence = connectionSocket.recv(1024).decode()
    connectionSocket.close()





def process_request(req):
    start_line, header_dict, header_body = get_dict_from_header(req)
    if check_version(start_line) == False:
        response_msg = "<h1>Invalid Version</h1>"
        print("Invalid version")
        return
    print('host_verify(header_dict)==0  = ' , host_verify(header_dict)==0)
    if host_verify(header_dict)==0:
        return "<h1>400</h1>"
    if start_line.startswith('GET'):
        print("GET method used")
        response_message = "HTTP/1.1 200 OK\r\n"
        response_message += "\r\n"
        file_content = handle_GET(start_line, header_dict, header_body)
        response_message += str(file_content)
        return response_message
    elif start_line.startswith('PUT'):
        print("PUT method used")
        response_message = "HTTP/1.1 200 OK\r\n"
        response_message += "\r\n"
        file_path = str(handle_PUT(start_line, header_dict, header_body))
        print("file path : ",file_path)
        print('----------------------')
        response_message += str(get_file_content_PUT(file_path))
        
        return response_message
    elif start_line.startswith('DELETE'):
        print("DELETE method used")
        response_message = "HTTP/1.1 200 OK\r\n"
        response_message += "\r\n"
        file_path = handle_DELETE(start_line, header_dict, header_body)
        response_message += str(get_file_content_DELETE(file_path))
        
        return response_message
        
    else:
        response_msg = "<h1>Invalid Method</h1>"
        print("Invalid method")





while True:
    connectionSocket, addr = serverSocket.accept()
    th = Thread(target = doIO_socket, args = (connectionSocket,))
    print("starting the thread");
    th.start()

    '''
    # connectionSocket.shutdown(socket.SHUT_WR)
    print(connectionSocket, addr)
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
    '''
    print("code ended")

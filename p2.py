
import socket,sys
return_response_dict = {'status code' : 120}

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
        
        
def handle_url(str):
    for i in str:
        if i==' ':
            return 0
        if i== '/':
            return 0
    return 1
        
def handle_header_host(dict):
    if 'host' in dict:
        if handle_url(dict['host'])==0:
            print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh\n\n")
            return_response_dict['status code']=400
            return_response_dict['status code message']='Bad Request'
        else:
            return_response_dict['host_path'] = dict['host']   # rempove port number from it!

    else:
        print('iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii\n\n')
        return_response_dict['status code']=400
        return_response_dict['status code message']='Bad Request'
    
        
def handle_headers(start_line,dict,header_body):
    return handle_header_host(dict)
    

# [1,2,3,4] [2:] --> [3,4]  [34]
        
message=''
message += "GET /Content/themes/basic/vendors/fastclick/lib/fastclick.js HTTP/1.1\r\n"
message += "Host: portal.coep.org.in:9093\r\n"
message += "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:126.0) Gecko/20100101 Firefox/126.0\r\n"
message += "Accept: */*\r\n"
message += "Accept-Language: en-US,en;q=0.5\r\n"
message += "Accept-Encoding: gzip, deflate\r\n"
message += "Connection: keep-alive\r\n"
message += "Referer: http://portal.coep.org.in:9093/\r\n"
message += "Cookie: _ga_TE06MZ3JNC=GS1.1.1717964486.13.0.1717964486.0.0.0; _ga=GA1.1.1329315096.1707154481; .ASPXAUTH=0D15AB82CCDBD503197BC7C48E097B77BCD90F741C664741DA8A1E989995819AF510267A4DDB1EA36E26D175EF2962E3127F8B3996D0095C2C4759744BBEC501747943D62668EA9445FFAC8DD298310732C7FDCC0C069CD0D50AE94C145D5BE0; ASP.NET_SessionId=0uc0dfz1ts2dckyahketgyux\r\n\r\n"





# header_body=''
# start_line,dict,header_body = get_dict_from_header(message)

# # handle_headers(start_line,dict,header_body)

# print('start line : ')
# print(start_line)
# print('dict : ')
# print(dict)
# print('body : ')
# print(header_body)

def run_server():
    print('in run server')
    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET , socket.SO_REUSEADDR,1)
    server_host = '127.0.0.1'
    server_port = 1060
    
        
    if sys.argv[1]=='server': 
        print('in server!')
        s.bind(('',server_port))

        s.listen(1) 
        # s.bind((server_host,server_port))
        print('listening')
        
        while True:
            server_socket , server_address = s.accept()
            data = server_socket.recv(1024)
            data = data.decode()
            msg=data
            # while data:
                # print(data)
                # data = server_socket.recv(1024)
                # if data is None:
                #     break
                # msg += data
            print('data has been recieved')
            start_line,dict,header_body = get_dict_from_header(msg)
            
            tp_response = (
                f"<html><body><h1>Received POST Request</h1>"
                f"<p>Request Body: {'hii, this is Arnav!'}</p></body></html>"
            )
            
            handle_headers(start_line,dict,header_body)
            if return_response_dict['status code']==400:
                tp_response = (
                    f"<html><body><h1>Received POST Request</h1>"
                    f"<p>Request Body: {'oops its an error!!'}</p></body></html>"
                )
            
            if return_response_dict.get('status code') == 400:
                tp_response_body = "<html><body><h1>Received POST Request</h1><p>Request Body: oops its an error!!</p></body></html>"
                tp_response_status = "HTTP/1.1 400 Bad Request\r\n"
            else:
                tp_response_body = "<html><body><h1>Received POST Request</h1><p>Request Body: hii, this is Arnav!</p></body></html>"
                tp_response_status = "HTTP/1.1 200 OK\r\n"
            
            tp_response_headers = (
                f"Content-Type: text/html\r\n"
                f"Content-Length: {len(tp_response_body)}\r\n"
                f"\r\n"
            )
            tp_response = tp_response_status + tp_response_headers + tp_response_body
                
            print('......................................')
            print(dict)
                
                
            
            
            server_socket.sendall(tp_response.encode())
            
            
            
        s.close()
        print('ended!')
            
    else:
        # client
        data = b'hi we have started our new server do use it!!!!'
        
        s.connect((server_host,server_port))
        s.sendall(data)
        print('data sent!')
            
    
            

if __name__ == '__main__':
    run_server()


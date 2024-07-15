import sys
sys.path.append('../')
from server.common import *
from common import *

'''
ADD MORE OPTIONS TO CHECK FOR URI VALIDITY
checks whether the given URI is valid or not
invalid URIs:
    should not contain whitespaces, tabs

    should not contain any '/'
    that is, URI should be absolute

returns 1:
    URI is valid
returns 0:
    URI is invalid
'''
def handle_uri(str):
    for i in str:
        if i==' ' or '\t':
            return 0
        if i== '/':
            return 0
    return 1

'''
handles the host header in HTTP/1.1 request
1. checks if the host header is present in it or not
   if not present, status code set to {400 : Bad request}
2. if the host exists, then validity of URI is checked
3. if the URI is valid, host path is saved
4. port number (if present) is extracted from the URI
5. by default, 80 is assumed as port number
'''
def handle_header_host(dict , shared_state):
    
    if 'host' in dict:
        if handle_uri(dict['host'])==0:
            shared_state.arr_global_return_status_code[0] = 400
            return_response_dict['host_path'] = "/ "
        else:
            # now we extract the port number of the host
            # this is after the colon in the URI
            uri_tokens = dict['host'].split(':')
            # print("dict['host'].split(':')[0]  = " , uri_tokens[0] )
            if len(uri_tokens)==2:
                # print("dict['host'].split(':')[1]  = " , dict['host'].split(':')[1] )
                return_response_dict['host_port'] = dict['host'].split(':')[1]
            else:
                return_response_dict['host_port'] = 80

            return_response_dict['host_path'] = dict['host'].split(':')[0]
            
    else:
        # set status code to {400 : Bad request}
        print_logs(6, 'handle_header_host', 'Host header NOT found in request', '', -1)
        shared_state.arr_global_return_status_code[0] = 400


'''
wrapper function for handle_header_host()
returns a boolean value based on the status code
this is done after calling handle_header_host
returns 0:
    status code == 400
returns 1:
    status code != 400 
'''
def host_verify(dict , shared_state):
    handle_header_host(dict , shared_state)
    if shared_state.arr_global_return_status_code[0] == 400:
        return 0
    return 1
        
        



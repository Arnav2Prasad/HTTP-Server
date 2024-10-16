# from ....server.common import *

import sys
sys.path.append('../')

from server.common import *

shared_state = SharedState()

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
            shared_state.global_return_status = 400
            return_response_dict['host_path'] = "/ "
        else:
            url_tokens = dict['host'].split(':')
            print("dict['host'].split(':')[0]  = " , url_tokens[0] )
            if len(url_tokens)==2:
                print("dict['host'].split(':')[1]  = " , dict['host'].split(':')[1] )
                return_response_dict['host_port'] = dict['host'].split(':')[1]
            else:
                return_response_dict['host_port'] = 80

            return_response_dict['host_path'] = dict['host'].split(':')[0]   # rempove port number from it!
            
    else:
        print('Host header NOT found (in handle_header_host)')
        shared_state.global_return_status = 400

def host_verify(dict):
    print("started verifiying (in host_verify)")
    print("dict :")
    print(dict)
    handle_header_host(dict)
    print('global return status (in host_verify): ' ,  shared_state.global_return_status)
    if shared_state.global_return_status == 400:
        return 0  #flag error status code
    return 1
        
        



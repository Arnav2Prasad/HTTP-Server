import sys
sys.path.append('../')


from server.common import *


'''
handle_connection
We check for 'connection' in header_dict:
    if doesnt exists --> dict['connection'] = keep-alive
    elif its keep-alive --> then = dict['connection'] = keep-alive
    elif its close --> then = dict['connection'] = close
    else:
        keep arr_global_return_status_code[0] = 400
'''
def handle_connection(header_dict , shared_state):
    # print_logs(5, "handle_connection", "entered function", "shared_state.return_response_dict", shared_state.return_response_dict)
    
    if 'connection' not in header_dict:
        shared_state.return_response_dict['connection']="keep-alive"    
    elif header_dict['connection'].lower()=="keep-alive":
        shared_state.return_response_dict['connection']="keep-alive"
    elif header_dict['connection'].lower()=="close":
        shared_state.return_response_dict['connection']="close"
    else:
        shared_state.arr_global_return_status_code[0] = 400
        
    # print_logs(5, "handle_connection", "after execution", "shared_state.return_response_dict", shared_state.return_response_dict)
    # print_logs(5, "handle_connection", "after execution", "shared_state.arr_global_return_status", shared_state.arr_global_return_status_code)
    
    
'''
We call handle_connection()
We then check for shared_state.arr_global_return_status_code 
    if its 400 -->
        return 0
    else:
        return 1
'''
    
def connection_verify(header_dict , shared_state):
    handle_connection(header_dict , shared_state)
    
    global_status_length = len(shared_state.arr_global_return_status_code)
    if global_status_length >=0 and shared_state.arr_global_return_status_code[0] == 400:
        return 0
    return 1
        
        
        

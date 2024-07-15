# from ....server.common import *

import sys
sys.path.append('../')

from server.common import *

        
import chardet

def detect_file_encoding(file_path):
    try:
        with open(file_path, 'rb') as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']
            print_logs(5, 'detect_file_encoding', '', 'encoding', encoding)
            return encoding
    except FileNotFoundError:
        print_logs(6, 'detect_file_encoding', 'file not found in detect', '', -1)
        return ''
    except Exception as e:
        print_logs(6, 'detect_file_encoding', 'exception---------   ', '', -1)
        return ''


            
def handle_parameters_accept_charset(shared_state , j):
    if 'file_path' not in shared_state.return_response_dict:
        print('j not in charset dict-----file path path path-- : j = ' , j)
        return 0
    
    if j=='*':
        print('j not in charset dict----***********--------- : j = ' , j)
        return 1
    
    if j not in charset_dict:
        print('j not in charset dict----------------- : j = ' , j)
        return 0
    
    if detect_file_encoding(shared_state.return_response_dict['file_path']) == charset_dict[j]:
        return 1
    else:
        return 0
        
        
    
    
        

   
            
def implement_accept_charset(shared_state):
    accept_charset_dict = shared_state.return_response_dict['accept-charset']
    if accept_charset_dict == {}:
        return
    
    print(shared_state.return_response_dict['accept-charset_q_val_list'])
    print_logs(6 , 'implement_accept_charset' , '++++++++++++++++' , '',-1)
    
    for i in shared_state.return_response_dict['accept-charset_q_val_list']:
        parameters = shared_state.return_response_dict['accept-charset'][i]
        for j in parameters:
            if handle_parameters_accept_charset(shared_state , j) == 1:
                return 1
            
    return 0
            
def handle_accept_charset(shared_state , header_dict):
    if 'accept-charset' not in header_dict:
        return
    
    header_extract_q_value(shared_state ,header_dict , 'accept-charset')
    if implement_accept_charset(shared_state) != 1:
        shared_state.arr_global_return_status_code[0] = 406
    
        
    
        
        
        
    
    
    
    
    
    
    
    
    
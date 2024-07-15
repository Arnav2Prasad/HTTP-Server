import sys
sys.path.append('../')


from server.common import *

'''
generic function to get the value of q ie for q=0.2
get 0.2.
The value of q-value should be 0 <= value <= 1 
Approach : 
    1. trim the q_val to remove any leading or trailing space
    2. if q_value if empty  --> its 1 (acc to rfc) 
                                and return from the function
    3. If q_value is invalid, we return void(ie return nothing)
            but marke  "q_value_undefined"  in shared_state as 1
    4. The same step(step-3) is done if q_value is >1 or <0
    5. Finally, if all constraints match, we append the q_value in the 
        'q_value' list and return (void)
'''
def handle_q_val(shared_state, q_val,q_val_list):
    q_val.strip()
    num=1
    if q_val == '':
        q_val_list.append(1)
        return 1
    if q_val[0]=='q' and q_val[1]=='=':
        try: 
            num = float(q_val[2:])
        except:
            shared_state.return_response_dict['q_value_undefined'] = 1
            return

    else:
        shared_state.return_response_dict['q_value_undefined'] = 1
    if num>1 or num < 0:
        shared_state.return_response_dict['q_value_undefined'] = 1
        return
        
    q_val_list.append(num)
        


'''
Its a generic function' --> taking header_name as input ie accept, accept_charset , etc
header_extract_q_value

1. we split on ',' the header_value from the header_dict
2. We run a loop, where we aim to get q:q->value
    We want a dictionary having q->value as keys and q as value
    and one more list of having q->values, we sort the list later.
    If q->value is >1 or <0 we dont consider the q for such case, and we 
    dont put it furthur in the dictionary and the list.
'''

# def header_extract_q_value(shared_state ,header_dict , header_name):
#     if header_name not in header_dict:
#         return

#     header_values = header_dict[header_name].split(',')
#     print_logs(5, 'header_extract_q_value' , '' , 'header_values' , header_values)
    
#     word=""
#     flag=False
#     q_val = ""
#     q_val_list=[]
#     dict = {}
    
#     # check for semicolon
#     for parameters in header_values:
#         # list of strings
#         parameters = parameters.strip()
#         if 'q_value_undefined' in shared_state.return_response_dict:
#             shared_state.return_response_dict.pop('q_value_undefined')
#         print_logs(5 , 'header_extract_q_value' , '' , 'parameters', parameters)
#         word=""
#         flag=False
#         q_val = ""
#         for i in parameters:
#             if i == ';':
#                 para = word
#                 word=""
#                 flag=True
#                 continue
#             word += i
#             if flag==True:
#                 q_val += i
#         if flag != True:
#             para = word
                
    
#         handle_q_val(shared_state , q_val , q_val_list)
        
#         if 'q_value_undefined' not in shared_state.return_response_dict:
#             if q_val_list[-1] in dict:
#                 dict[q_val_list[-1]].append(para)
#             else:
#                 dict[q_val_list[-1]] = []
#                 dict[q_val_list[-1]].append(para)
        
#     shared_state.return_response_dict[header_name] = dict
    
#     q_val_list.sort(reverse = True)
#     shared_state.return_response_dict[header_name + '_q_val_list'] = q_val_list
    
#     print_logs(5 , 'header_extract_q_value' , '' , 'shared_state.return_response_dict' , shared_state.return_response_dict )
        

'''
With this function,
    we map the accept extension to the file type
    
    if q is text/html  and file is 'file'
        then we look 'file' + '.html' in the path and check its existence.
        
    if q is of form ../* ie text/*
        we lool for 'text/' in the dict, and seacrh for all values in the dict 
        that contains 'text/' in it. Further we form patterns and check its
        existence in path.
        
    We get the file extension via mime_types dictionary , and further check for it in path
    if q is invalid, we ignore it
    
    Format : 
            file_name + '.' + file_extension
    
'''
            
def handle_parameters_extension(shared_state , j):
    if 'temp_file_path' not in shared_state.return_response_dict:
        return ''
    
    if j[-1] =='*':
        j_not_star = j[:-1]
        for tmp in mime_types:
            if j_not_star in tmp:
                destination_file_path = shared_state.return_response_dict['temp_file_path'] + '.' + mime_types[tmp][0]
                print_logs(5 , 'handle_parameters_extension' , '' , 'destination_file_path' , destination_file_path)
                if os.path.exists(destination_file_path):
                    shared_state.return_response_dict['file_path'] = destination_file_path
                    return destination_file_path
                
                
    
    if j not in mime_types:
        return ''
    
    
        
    destination_file_path = shared_state.return_response_dict['temp_file_path'] + '.' + mime_types[j][0]
    print_logs(5 , 'handle_parameters_extension' , '' , 'destination_file_path' , destination_file_path)
    if os.path.exists(destination_file_path):
        shared_state.return_response_dict['file_path'] = destination_file_path
        return destination_file_path
    else:
        return ''
    

'''
implement accept
we get the value of 'accept dictionary' from shared_state.return_response_dict
    if accept_dictionary is empty we return (void)
    
    Now we iterate to the list of all sorted values present in accept_q_val_list
        and get the q->val and so use this q->val to get the list of keys
        containg values of 'q'.
        
        Now we iterate that list, having lables of 'q' (not q->value) and 
        call ' handle_parameters_extension ' for each of them.
        As soon as we find a file exists in path, we will return it
'''
            
def implement_accept(shared_state):
    accept_dict = shared_state.return_response_dict['accept']
    if accept_dict == {}:
        return

    
    for i in shared_state.return_response_dict['accept_q_val_list']:
        parameters = shared_state.return_response_dict['accept'][i]
        for j in parameters:
            if handle_parameters_extension(shared_state , j) != '':
                return
  
  
  
  
'''
handle_accept
We check for accept in header_dict
    if not present , return (void)
    else call further functions
'''            
def handle_accept(shared_state , header_dict):
    if 'accept' not in header_dict:
        return
    
    header_extract_q_value(shared_state ,header_dict , 'accept')
    implement_accept(shared_state)
    
        
        
        
    
    
    
    
    
    
    
    
    
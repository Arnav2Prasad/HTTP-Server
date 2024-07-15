import sys
sys.path.append('../')


from server.common import *


'''
handle_content_type()
this function takes file_path from the shared_state.return_response_dict
We split the file_path on .
NOTE : We assumed file extension are there always after last .  
        ie file.txt has extension  ' txt ' 
        or a.b.c here file extension is ' c '
        

If file_path doesnt exists :
    check for the last word(thats l[-1]) :
    if its there in the dictonary 
        get the file_extensions from the mime_types_reversed and put it in the 
        content-type
    if not --> content-type = text/html
    
If file_path doesnt exists :
    content-type = text/html

'''            
def handle_content_type(shared_state):
    file_path = shared_state.return_response_dict['file_path']
    l = file_path.split('.')
    if len(l) == 1:
        shared_state.return_response_dict['content_type'] = 'text/html'
    else:
        if l[-1] in mime_types_reversed:
            shared_state.return_response_dict['content_type'] = mime_types_reversed[l[-1]]
        else:
            shared_state.return_response_dict['content_type'] = 'text/html'
             
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
           
    
    
    
        
        
        
    
    
    
    
    
    
    
    
    
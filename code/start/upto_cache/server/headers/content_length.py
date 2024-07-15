import sys
sys.path.append('../')

from server.common import *


'''
handle_content_length()
this function checks for length of response_body(thats stored in shared_state)
if response_body exists --> return its length
else:  return -1
'''            
def handle_content_length(shared_state):
    if 'response_body' in shared_state.return_response_dict:
        return len(shared_state.return_response_dict['response_body'])
    return -1
    
    
        
        
        
    
    
    
    
    
    
    
    
    
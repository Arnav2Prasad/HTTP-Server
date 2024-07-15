# from ....server.common import *
'''
this file contains all the necessary functions related
to the last-modified header field in HTTP/1.1 response

'''
import sys
sys.path.append('../')

from server.common import *

'''
returns the timestamp of a file whose path is "file_path"
timestamp is converted into rfc 822 format
'''
def last_modified_file_timestamp(file_path):
    # get the modification timestamp of the file
    timestamp = os.path.getmtime(file_path)

    # convert the timestamp to RFC 822 format
    rfc_822_time = email.utils.formatdate(timestamp, localtime=False)

    # replace the last 5 bytes of the time with "GMT"
    rfc_822_time = rfc_822_time[:-5] + "GMT"

    return rfc_822_time

'''
this is a wrapper function for last_modified_file_timestamp()
uses the file_path value in return_response_dict
'''
def handle_last_modified_file_path(shared_state):
    # print(shared_state.return_response_dict)
    print_logs(5, 'handle_last_modified' , '','shared_state.return_response_dict', shared_state.return_response_dict )
    
    return last_modified_file_timestamp(shared_state.return_response_dict['file_path'])

'''
wrapper function for last_modified_file_timestamp()
uses the backup_file_path value in return_response_dict
'''  
def handle_last_modified_backup(shared_state):
    # print(shared_state.return_response_dict)
    print_logs(5, 'handle_last_modified' , '','shared_state.return_response_dict', shared_state.return_response_dict )
    
    return last_modified_file_timestamp(shared_state.return_response_dict['backup_file_path'])
    


    

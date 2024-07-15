import os
import email.utils
from datetime import datetime  
from email.utils import parsedate_to_datetime
import sys
sys.path.append('../')
from server.common import * 
from headers.date import *

'''
function should be removed and placed in ../common.py
'''
def datetime_to_rfc_822(dt):
    # Parse the string into a datetime object
    dt = datetime.strptime(dt, '%a, %d %b %Y %H:%M:%S GMT')
    
    # Ensure the datetime is in GMT
    dt = dt.astimezone(tz=datetime.now().astimezone().tzinfo)
    
    # Format the datetime as RFC 822
    return dt.strftime('%a, %d %b %Y %H:%M:%S GMT')

'''
function should be removed and placed in ../common.py
'''
def get_file_modify_timestamp(file_path):
    # Get the modification timestamp of the file
    timestamp = os.path.getmtime(file_path)

    # Convert the timestamp to RFC 822 format
    rfc_822_time = email.utils.formatdate(timestamp, localtime=False)
    rfc_822_time = rfc_822_time[:-5] + "GMT"

    print_logs(5, "un_get_file_modify_timestamp", "The file's modification time in RFC 822 format is :", "rfc_822_time", rfc_822_time)
    # print(f"The file's modification time in RFC 822 format: {rfc_822_time}")
    return rfc_822_time
    

  
'''
compares two timestamps, input_time and file_time

this is used for the if-modified-since header,
and hence comparison results are as follows
    returns 1:
       inputted time is earlier than file_time
       eg. input_time = Sep 2024
           file_time = Nov 2024
    returns -1:
        inputted time is later than file_time
       eg. input_time = Nov 2024
           file_time = Sep 2024
'''
def if_modified_compare_time_stamp(input_time,file_time):
    input_time_dt = parsedate_to_datetime(input_time)
    file_time_dt = parsedate_to_datetime(file_time)
    
    # Compare the datetime objects
    if input_time_dt > file_time_dt:
        return -1
    return 1


''' 
handles the if-modified-since header in HTTP/1.1 request
    1. checks if the if-unmodified-since header was present
       in the response.
       If not present, -1 is returned
    2. checks for the validity of date
       If invalid date is given, 1 is returned
    3. compares the file modification time and input time
       returns appropriate results
'''
def handle_if_modified_since(dict,file_path,shared_state):
    print_logs(5, "handle_if_modified_since", "", "dict", dict)

    # check if if-modified-since header is in request
    if 'if-modified-since' in dict:
        if if_headers_handle_date(dict['if-modified-since']) == 0:
            shared_state.arr_global_return_status_code[0] = 200
            return 1
            
 
        # convert date time from rfc822 to regular
        # this is the time that is requested by the client
        # the response should be unmodified since this time
        req_if = datetime_to_rfc_822(dict['if-modified-since'])

        # get the file_time from file with path "file_path"
        file_time = get_file_modify_timestamp(file_path)
        
        # compare the two time stamps
        if if_modified_compare_time_stamp(req_if,file_time) == 1:
            # this means that file is unmodified since req_if
            # that is, req_if > file_time
            shared_state.return_response_dict['is_modified'] = True
            shared_state.arr_global_return_status_code[0] = 200
            return 1
        else:
            # this means that the file is modified since req_if
            # that is, req_if < file_time
            shared_state.return_response_dict['is_modified'] = False
            shared_state.arr_global_return_status_code[0] = 304
            return 0
    else:
        print_logs(6, "handle_if_modified_since", "if-modified-since header not found", "", -1)
        return -1

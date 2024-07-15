import os
import email.utils
from datetime import datetime  
from email.utils import parsedate_to_datetime
import sys
sys.path.append('../')
from server.common import * 
from headers.date import *

# ----------IMP----------
# MAKE CHANGES TO THE CONDITION WHEN IF-UNMODIFIED-SINCE IS NOT MET
# {412 : PRECONDITION} SHOULD BE GIVEN, INSTEAD OF {304 : NOT MODIFIED}

'''
this file contains all the necessary functions related
to the if-unmodified-since header field in HTTP/1.1 response
'''

'''
function should be removed and placed in ../common.py
'''
# format conversion
# converts datetime to rfc 822 format
# example of rfc 822 format is
def datetime_to_rfc_822(dt):
    # parse the string into a datetime object
    dt = datetime.strptime(dt, '%a, %d %b %Y %H:%M:%S GMT')
    
    # ensure the datetime is in GMT
    dt = dt.astimezone(tz=datetime.now().astimezone().tzinfo)
    
    # format the datetime as RFC 822
    return dt.strftime('%a, %d %b %Y %H:%M:%S GMT')

# gets the file modification timestamp of file 
# whose path is file_path
'''
function should be removed and placed in ../common.py
'''
def un_get_file_modify_timestamp(file_path):
    # get the modification timestamp of the file
    timestamp = os.path.getmtime(file_path)

    # convert the timestamp to RFC 822 format
    rfc_822_time = email.utils.formatdate(timestamp, localtime=False)
    rfc_822_time = rfc_822_time[:-5] + "GMT"

    return rfc_822_time
   
'''
compares two timestamps, input_time and file_time

this is used for the if-unmodified-since header,
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
def if_unmodified_compare_time_stamp(input_time,file_time):

    input_time_dt = parsedate_to_datetime(input_time)
    file_time_dt = parsedate_to_datetime(file_time)
    
    # compare the datetime objects
    if input_time_dt < file_time_dt:
        return -1
    return 1


''' 
handles the if-unmodified-since header in HTTP/1.1 request
    1. checks if the if-unmodified-since header was present
       in the response.
       If not present, -1 is returned
    2. checks for the validity of date
       If invalid date is given, 1 is returned
    3. compares the file modification time and input time
       returns appropriate results
'''
def handle_if_unmodified_since(dict,file_path,shared_state):
    print_logs(5, "handle_if_unmodified_since", "", "dict", dict)
    

    # check if if-unmodified-since header is in request
    if 'if-unmodified-since' in dict:
        if if_headers_handle_date(dict['if-unmodified-since']) == 0:
            shared_state.arr_global_return_status_code[0] = 200
            return 1
        
        # convert date time from rfc822 to regular
        # this is the time that is requested by the client
        # the response should be unmodified since this time
        req_if = datetime_to_rfc_822(dict['if-unmodified-since'])

        # get the file_time from file with path "file_path"
        file_time = un_get_file_modify_timestamp(file_path)
        
        # compare the two time stamps
        if if_unmodified_compare_time_stamp(req_if,file_time) == 1:
            # this means that file is unmodified since req_if
            # that is, req_if > file_time
            shared_state.return_response_dict['is_unmodified'] = True

            # set status code to {200 : OK}
            shared_state.arr_global_return_status_code[0]=200
            return 1
        else:
            # this means that file has been modified since req_if
            # that is, req_if < file_time
            shared_state.return_response_dict['is_unmodified'] = False

            # set status code to {412 : Precondition Failed}
            shared_state.arr_global_return_status_code[0] = 304
            return 0
    else:
        print_logs(6, "handle_if_un_modified_since", "if-unmodified-since header not found", "", -1)
        return -1

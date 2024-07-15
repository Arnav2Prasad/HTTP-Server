import sys
from datetime import datetime, timezone
sys.path.append('../')

    
from datetime import datetime
import re


'''
This function validates a date string according to RFC 822 format.
'''
def validate_date_rfc822(date_str):
    try:
        # Try to parse the date string using the RFC 822 format.
        datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S %Z')
        return True
    except ValueError:
        # If parsing fails, it means the date string is not in RFC 822 format.
        return False



'''
This function validates a date string according to RFC 850 format.
'''
def validate_date_rfc850(date_str):
    try:
        # Try to parse the date string using the RFC 850 format.
        datetime.strptime(date_str, '%A, %d-%b-%y %H:%M:%S %Z')
        return True
    except ValueError:
        # If parsing fails, it means the date string is not in RFC 850 format.
        return False


'''
This function validates a date string according to ASCII time (asctime) format.
'''
def validate_date_asctime(date_str):
    try:
        # Try to parse the date string using the asctime format.
        datetime.strptime(date_str, '%a %b %d %H:%M:%S %Y')
        return True
    except ValueError:
        # If parsing fails, it means the date string is not in asctime format.
        return False


'''
This function checks the 'date' key in a dictionary and validates its format.
'''
def handle_date(dict):
    if 'date' in dict:
        if validate_date_rfc822(dict['date']):
            # If the date is in RFC 822 format
            print(f"{dict['date']} is a valid RFC 822 date format.")
            return 1
        elif validate_date_rfc850(dict['date']):
            # If the date is in RFC 850 format
            print(f"{dict['date']} is a valid RFC 850 date format.")
            return 1
        elif validate_date_asctime(dict['date']):
            # If the date is in asctime format
            print(f"{dict['date']} is a valid Ascii Time (asctime) date format.")
            return 1
        else:
            # If the date is not in any recognized format
            print(f"{dict['date']} is not a recognized valid date format.")
            return 0
    else:
        # If the 'date' key is not in the dictionary
        return 0
    
    
'''
This function validates an input date string against RFC 822, RFC 850, and asctime formats.
'''
def if_headers_handle_date(input_date):
    
    if validate_date_rfc822(input_date):
        print(f"{input_date} is a valid RFC 822 date format.")
        return 1
    elif validate_date_rfc850(input_date):
        print(f"{input_date} is a valid RFC 850 date format.")
        return 1
    elif validate_date_asctime(input_date):
        print(f"{input_date} is a valid Ascii Time (asctime) date format.")
        return 1
    else:
        print(f"{input_date} is not a recognized valid date format.")
        return 0
    
    
    
'''
This function creates a timestamp in the current UTC time formatted according to RFC 7231.
'''
def create_time_stamp(shared_state):
    # Get the current UTC time
    current_utc_time = datetime.now(timezone.utc)

    # Format the date as per HTTP RFC (RFC 7231) in GMT
    rfc7231_date = current_utc_time.strftime('%a, %d %b %Y %H:%M:%S GMT')
    
    # Store the formatted date in the shared_state's return_response_dict under the 'Date' key
    shared_state.return_response_dict['Date'] = rfc7231_date
    
    





        
        

#!/usr.bin.python
# th = Thread(target = add, args = (i, matorder, mat1, mat2, mat3))
import socket
from threading import Thread
import shutil
from datetime import datetime

# global_return_status = 200
return_response_dict={}

# singleton.py
class SharedState:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.global_return_status = 203
        return cls._instance


def get_file_name(start_line):
    file_name = start_line.split('/')
    print("file_name : " , file_name[-1])
    return file_name[-1]

def get_file_path(start_line):
    tokens = start_line.split(' ')
    print("tokens[1] = ", tokens[1])
    return tokens[1]

def check_version(start_line):
    tokens = start_line.split(' ')
    return tokens[2] == "HTTP/1.1"

def mov_file(source_path,destination_path):
    try:
        shutil.move(source_path, destination_path)
        print(f"File moved from {source_path} to {destination_path} successfully.")
    except FileNotFoundError:
        print(f"The file {source_path} does not exist.")
    except PermissionError:
        print(f"Permission denied: Unable to move {source_path}.")
    except Exception as e:
        print(f"Error: {e}")
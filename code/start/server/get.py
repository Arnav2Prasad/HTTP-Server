from common import *

def handle_GET(start_line, header_dict, header_body):
    file_path = get_file_path(start_line)
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print("file content is :\n", content)
        return content
    except Exception as e:
        print("an error occured : ", e)
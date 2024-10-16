from common import *

def handle_PUT(start_line, header_dict, header_body):
    file_path = get_file_path(start_line)
    print("file path : (in handle put) ",file_path)

    # Open the file in write mode
    with open(file_path, "w") as file:
        # Write some content to the file
        file.write(header_body)

    print(f"File created at (in handle put) :  {file_path}")
    return file_path

def get_file_content_PUT(file_path):
    print("file path in get file content : ",file_path)
    # file_path = get_file_path(start_line)
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        print("file content is :\n", content)
        return content
    except Exception as e:
        print("an error occured in get file content put: ", e)
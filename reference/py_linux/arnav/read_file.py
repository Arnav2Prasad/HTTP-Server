# Define the path to the file
file_path = "/home/arnav/py_linux/create_dir.py"

# Open and read the content of the file
try:
    with open(file_path, 'r') as file:
        content = file.read()
    print("File content retrieved successfully.")
    print(content)
except Exception as e:
    print(f"An error occurred: {e}")

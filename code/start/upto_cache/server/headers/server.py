import subprocess

'''
run_uname is used to call the linux command 'uname -op'
uname prints the system information of the the server
-o prints the OS type
-p prints the processor type

server header in HTTP/1.1 uses this command to give
information about the server machine to the client

'''
def run_uname():
    try:
        # Run the `uname -a` command
        result = subprocess.run(['uname', '-op'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        # Print the output
        return result.stdout[:-1]
    except subprocess.CalledProcessError as e:
        print('Error:', e.stderr)

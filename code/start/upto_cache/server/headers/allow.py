'''
directly implemented in main.py
Approach : 
    First check the request start word ie GET, HEAD, PUT, etc
    if its there in http_methods proceed furthur for analysis of request 
    Else return  Invalid Method (406) ie dont go for furthur analysis of request. 
'''


http_methods = ['GET' , 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE', 'PATCH']



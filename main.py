import socket
from views import home_page,calc_total

URLS = { 
    '/':home_page,
    '/total':calc_total
    }

def parse_request(req):    
    data = req.split(' ')    
    method = data[0]
    url = data[1]
    return (method,url)
    

def generate_headers(method,url):
    status = None
    
    if method !='GET':
        status = 405 
        return ('HTTP/1.1 405 Method not allowed\n\n',status)
    if url not in URLS:
        status  = 404
        return ('HTTP/1.1 404 Page not found\n\n',status)
    status = 200
    return ('HTTP/1.1 200 OK\n\n',status)    
        
def generate_content(code,url):
    if code == 404:
        return '<h1>Page not found</h1>'
    if code == 405:
        return '<h1>Method not allowed</h1>'    
    if code == 200:
        return URLS[url]()  

def generate_response(request):
    method,url = parse_request(request)
    headers,code  = generate_headers(method,url)
    body = generate_content(code,url)    
    return (headers + body).encode()
   
   

def run():
    HOST = 'localhost' # can be just ''
    PORT = 8080
    BUF_SIZE = 1024
    ADDR = (HOST,PORT)
    # server side socket: uses 2 protocols (AF_INET,SOCK_STREAM)
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # to prevent 1.5 min block in case of extra activities
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_socket.bind(ADDR)
    # are there packages
    print('connected from',ADDR)
    server_socket.listen(5)

    while True:
        # suddenly a package! look at it and unpack this tuple return object socket but this time from client
        client_socket,addr = server_socket.accept()
        request = client_socket.recv(BUF_SIZE) # bytes in 1 package (1024)
        if not request:
            break
        # addr  ('127.0.0.1', 53881)
        # sockets don't understand str |=> bytes (method encode return bytes)
        response = generate_response(request.decode('utf-8'))
        print('response',response) # response b'HTTP/1.1 200 OK\n\ntata greets'
        client_socket.sendall(response)
        client_socket.close()

"""
# without decode of request (see in request_before_decode.txt (full request)
b'GET / HTTP/1.1\r\n
Host: 127.0.0.1:5000\r\n 
###############################
GET / HTTP/1.1
Host: 127.0.0.1:5000
"""

if __name__ == '__main__':
    print('start')
    run()
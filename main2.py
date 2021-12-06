import socket
import time

   
   

def run():
    HOST = 'localhost' # can be just ''
    PORT = 8080
    BUF_SIZE = 1024
    ADDR = (HOST,PORT)    
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)    
    server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    server_socket.bind(ADDR)   
    print('connected from',ADDR)
    server_socket.listen(5)

    while True:  
        print('listening...')     
        client_socket,addr = server_socket.accept()
        request = client_socket.recv(BUF_SIZE) # bytes in 1 package (1024)
        print('got a request',request)
        if not request:
            break
        print("ADDR",addr)
        # addr  ('127.0.0.1', 53881)
        response = f'Time now is: {time.ctime()} for your request: {request}'
        print('resp',response) 
        resp = response.encode()       
        client_socket.send(resp)
        client_socket.close()


if __name__ == '__main__':
    print('main2 is active at the moment')
    run()
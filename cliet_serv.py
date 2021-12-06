from socket import *

def run():
    HOST = 'localhost' # can be just ''
    PORT = 8080
    BUF_SIZE = 1024
    ADDR = (HOST,PORT)    
    client_socket = socket(AF_INET,SOCK_STREAM)
    client_socket.connect(ADDR)  
    
    while True:
        data = input('Enter your word: ').encode()         
        if not data:
            break        
        data = client_socket.send(data)
        data = client_socket.recv(BUF_SIZE)
        if not data:
            break
        else:
            print('encoded data',data)
            print('decoded data',data.decode('utf-8'))
    client_socket.close()


if __name__ == '__main__':
    run()
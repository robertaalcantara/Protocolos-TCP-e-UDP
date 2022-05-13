import socket
import time 
import sys

def TCP_client(tamanho, HEADER_SIZE):
    s = socket.socket()         # Create a socket object
    host = "123.123.123.123"    
    port = 55443                # Reserve a port for your service.

    t0 = time.time()
    f = open('pokemon.txt','rb')
    l = f.read(tamanho-HEADER_SIZE)
    s.connect((host, port))
    while (l):
        s.send(l)
        time.sleep(sys.float_info.min)
        l = f.read(tamanho-HEADER_SIZE)
    s.shutdown(socket.SHUT_WR)
    s.close()
    f.close()
    t1 = time.time()

    return t1-t0

TCP_client(1000, 54)
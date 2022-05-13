import socket
import time 
import sys

def TCP_client(tamanho, HEADER_SIZE):
    s = socket.socket()         # Create a socket object
    host = "123.123.123.123"    
    port = 55443                # Reserve a port for your service.
    f = open('pokemon.txt','rb')
    contador_pacotes = 0

    t0 = time.time()
    l = f.read(tamanho-HEADER_SIZE)
    s.connect((host, port))
    while (l):
        s.send(l)
        contador_pacotes+=1
        time.sleep(sys.float_info.min)
        l = f.read(tamanho-HEADER_SIZE)
    s.shutdown(socket.SHUT_WR)
    s.close()
    t1 = time.time()
    f.close()

    return t1-t0, contador_pacotes

TCP_client(1000, 54)
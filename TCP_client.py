import socket
import time 
import sys

def TCP_client(tamanho, HEADER_SIZE):
    s = socket.socket()         
    host = "123.123.123.123"    
    port = 55443               
    f = open('arquivo.txt','rb')
    contador_pacotes = 0

    t0 = time.time()
    s.connect((host, port))
    l = f.read(tamanho-HEADER_SIZE)
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
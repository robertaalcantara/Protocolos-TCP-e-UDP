import socket
import time

HOST = "123.123.123.123"  
PORT = 55443  

def TCP_server(tamanho, HEADER_SIZE, extra_sleep):
    f = open('arquivo_recebido.txt', 'wb')
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        
        conn, addr = s.accept()
        l = conn.recv(tamanho - HEADER_SIZE)
        while(l):
            f.write(l)
            l = conn.recv(tamanho - HEADER_SIZE)
        if extra_sleep:
            time.sleep(5)
        f.close()
        conn.close()
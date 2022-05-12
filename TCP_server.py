import socket
import time

HOST = "123.123.123.123"  # Standard loopback interface address (localhost)
PORT = 54321  # Port to listen on (non-privileged ports are > 1023)

def TCP_server(tamanho, HEADER_SIZE):
    f = open('arquivo_recebido.txt', 'wb')
    t0 = time.time()
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        l = conn.recv(tamanho - HEADER_SIZE)
        while(l):
            f.write(l)
            l = conn.recv(tamanho - HEADER_SIZE)
        f.close()
        conn.close()
    t1 = time.time()

    return t1-t0

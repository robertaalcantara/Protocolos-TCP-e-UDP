# echo-server.py

import socket
import time

HOST = "123.123.123.123"  # Standard loopback interface address (localhost)
PORT = 54321  # Port to listen on (non-privileged ports are > 1023)

f = open('arquivo_recebido.txt', 'wb')
i=0

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    l = conn.recv(946)
    while(l):
        print(l)
        f.write(l)
        l = conn.recv(946)
        time.sleep(0.1)
        i+=1
        if i==10:
            break
    f.close()
    conn.close()

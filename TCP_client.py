import socket 

def TCP_client(tamanho, HEADER_SIZE):
    s = socket.socket()         # Create a socket object
    host = "123.123.123.123"    
    port = 54321                # Reserve a port for your service.

    s.connect((host, port))
    f = open('arquivo.txt','rb')
    l = f.read(tamanho-HEADER_SIZE)
    while (l):
        s.send(l)
        l = f.read(tamanho-HEADER_SIZE)
    f.close()
    print ("Done Sending")
    s.shutdown(socket.SHUT_WR)
    s.close()

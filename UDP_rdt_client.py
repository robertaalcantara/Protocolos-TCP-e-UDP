import socket
import time

#msgFromClient       = "Hello UDP Server"
#bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("123.123.123.123", 55443)

def UDP_rdt_client(tamanho, HEADER_SIZE):
    # Create a UDP socket at client side
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    f = open('pokemon.txt','rb')
    contador_pacotes = 0

    t0 = time.time()
    l = f.read(tamanho-HEADER_SIZE)
    print(str(l))
    while (l):
        s.sendto(l, serverAddressPort)
        contador_pacotes+=1
        l = f.read(tamanho-HEADER_SIZE)

    t1 = time.time()
    f.close()

    return t1-t0, contador_pacotes

def close_UDP_rdt():
    bytesToSend = str.encode("CRm0W>W?;GQ4AP.sSg")
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.sendto(bytesToSend, serverAddressPort)

UDP_rdt_client(100,42)
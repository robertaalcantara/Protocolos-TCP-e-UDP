import socket

localIP     = "123.123.123.123"
localPort   = 55443

def UDP_server(bufferSize):
    UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    UDPServerSocket.bind((localIP, localPort))

    f = open('arquivo_recebido.txt', 'wb')

    while(True):
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]

        f.write(message)

UDP_server(1024)
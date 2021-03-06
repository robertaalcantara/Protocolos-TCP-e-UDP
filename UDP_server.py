import socket

localIP = "123.123.123.123"
localPort = 55443

def UDP_server(tamanho, HEADER_SIZE):
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.bind((localIP, localPort))

    f = open('arquivo_recebido.txt', 'wb')

    udp_open = True

    while(udp_open):
        bytesAddressPair = s.recvfrom(tamanho - HEADER_SIZE)
        message = bytesAddressPair[0]

        if message.decode('utf-8') == 'CRm0W>W?;GQ4AP.sSg':
            udp_open = False
        else:
            f.write(message)

    f.close()
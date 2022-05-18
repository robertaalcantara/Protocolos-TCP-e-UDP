import socket
import time
import numpy as np

serverAddressPort = ("123.123.123.123", 55443)

def get_checksum(l):
    binary_string = "".join(f"{ord(i):08b}" for i in l.decode('utf-8'))
    word_size_in_bits = (len(l)//3)*8
    word_size_in_bytes = len(l)//3

    binary_string = binary_string.zfill(word_size_in_bits*3)

    c1 = binary_string[0:word_size_in_bits]
    c2 = binary_string[word_size_in_bits:2*word_size_in_bits]
    c3 = binary_string[word_size_in_bits*2:word_size_in_bits*3]

    sum = bin(int(c1,2)+int(c2,2)+int(c3,2))[2:]

    if(len(sum)>word_size_in_bits):
        x = len(sum)-word_size_in_bits
        sum = bin(int(sum[:x], 2) + int(sum[x:],2))[2:]
    if(len(sum)<word_size_in_bits):
        sum = '0'*(word_size_in_bits-len(sum))+sum

    checksum = ''
    for i in sum:
        if(i=='1'):
            checksum += '0'
        else:
            checksum += '1'

    pacote_string = c1+c2+c3
    pacote = ''

    for i in range(len(pacote_string)//8):
        byte = pacote_string[i*8:(i+1)*8]    
        pacote += chr(int(byte,2))

    #checkson_0 = '0'
    #checkson_1 = '0'
    checksons = []
    for i in range(int(np.ceil(word_size_in_bytes/7))):
        checksons.append('0')
    
    #print(f"checkson list : {checksons}")

    for i in range(len(checksum)//8):
        byte = checksum[i*8:(i+1)*8]
        if byte[0] == '1':      #estouro de representação do checksum
            #if i<(len(checksum)//16):
            #    checkson_0 += '1'
            #else:
            #    checkson_1 += '1'
            checksons[i//7] += '1'
            byte = '0' + byte[1:]
        else:
            checksons[i//7] += '0'
            #if i<(len(checksum)//16):
            #    checkson_0 += '0'
            #else:
            #    checkson_1 += '0'  
        pacote += chr(int(byte,2))  

    for checkson in checksons:
        pacote += chr(int(checkson,2))
    #pacote += chr(int(checkson_0,2))
    #pacote += chr(int(checkson_1,2))

    #print(f"ultimo checkson {checksons[-1]}")
    
    return pacote.encode()

def UDP_rdt_client(tamanho, HEADER_SIZE):
    # Create a UDP socket at client side
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    f = open('arquivo.txt','rb')
    contador_pacotes = 0
    word_size = (tamanho-HEADER_SIZE)//4

    while((np.ceil(word_size/7) + word_size*4)>(tamanho-HEADER_SIZE)):
        word_size -= 1
    
    #print(f"word_size: {word_size}")

    t0 = time.time()
    l = f.read(word_size*3)
    if(len(l)==word_size*3):
        pacote = get_checksum(l)
    else:
        pacote = l
    
    while (l):
        s.sendto(pacote, serverAddressPort)
        contador_pacotes+=1

        ackResponse = s.recvfrom(tamanho - HEADER_SIZE)
        message = ackResponse[0]
        message_content = message.decode('utf-8')

        if message_content == 'ACK':
            l = f.read(word_size*3)
            if(len(l)==word_size*3):
                pacote = get_checksum(l)
            else:
                pacote = l
        else:
            continue
            
    t1 = time.time()
    f.close()

    return t1-t0, contador_pacotes

def close_UDP_rdt():
    bytesToSend = str.encode("CRm0W>W?;GQ4AP.sSg")
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.sendto(bytesToSend, serverAddressPort)
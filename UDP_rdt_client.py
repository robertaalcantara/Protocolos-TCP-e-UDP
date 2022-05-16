import socket
import time

serverAddressPort = ("123.123.123.123", 55443)

def get_checksum(l):
    binary_string = "".join(f"{ord(i):08b}" for i in l.decode('utf-8'))
    word_size_in_bits = (len(l)//3)*8

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

    checkson_0 = '0'
    checkson_1 = '0'

    for i in range(len(checksum)//8):
        byte = checksum[i*8:(i+1)*8]
        if byte[0] == '1':      #estouro de representação do checksum
            if i<(len(checksum)//16):
                checkson_0 += '1'
            else:
                checkson_1 += '1'
            byte = '0' + byte[1:]
        else:
            if i<(len(checksum)//16):
                checkson_0 += '0'
            else:
                checkson_1 += '0'  
        pacote += chr(int(byte,2))  

    pacote += chr(int(checkson_0,2))
    pacote += chr(int(checkson_1,2))

    return pacote.encode()

def UDP_rdt_client(tamanho, HEADER_SIZE):
    # Create a UDP socket at client side
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    f = open('pokemon.txt','rb')
    contador_pacotes = 0
    word_size = (tamanho-HEADER_SIZE)//4

    t0 = time.time()
    l = f.read(word_size*3)
    if(len(l)==word_size*3):
        pacote = get_checksum(l)
    else:
        pacote = l
    
    while (l):
        #print(pacote)
        #print(len(pacote))
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
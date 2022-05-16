import socket

localIP = "123.123.123.123"
localPort = 55443

def verify_checksum(message):
    binary_string = "".join(f"{ord(i):08b}" for i in message.decode('utf-8'))
    word_size_in_bits = (len(message)//4)*8

    binary_string = binary_string.zfill(word_size_in_bits*4)

    c1 = binary_string[:word_size_in_bits]
    c2 = binary_string[word_size_in_bits:word_size_in_bits*2]
    c3 = binary_string[word_size_in_bits*2:word_size_in_bits*3]

    sum = bin(int(c1,2)+int(c2,2)+int(c3,2))[2:]

    if(len(sum)>word_size_in_bits):
        x = len(sum)-word_size_in_bits
        sum = bin(int(sum[:x], 2) + int(sum[x:],2))[2:]
    if(len(sum)<word_size_in_bits):
        sum = '0'*(word_size_in_bits-len(sum))+sum

    checksum = binary_string[word_size_in_bits*3:word_size_in_bits*4]
    checksons = binary_string[word_size_in_bits*4:]
    
    for i in range(len(checksons)):
        if i==0 or i == 8:
            continue
        elif checksons[i] == '1':
            if i < 8:
                checksum = checksum[:(i-1)*8]+'1'+checksum[((i-1)*8)+1:]
            else:
                checksum = checksum[:(i-2)*8]+'1'+checksum[((i-2)*8)+1:]

    final_sum = bin(int(sum,2)+int(checksum,2))[2:]

    for char in final_sum:
        if char == '0':
            return False, ''
    
    return True, message[:(len(message)//4)*3]

def UDP_rdt_server(tamanho, HEADER_SIZE):
    s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    s.bind((localIP, localPort))

    with open('arquivo_recebido.txt', 'wb') as f:
        udp_open = True

        while(udp_open):
            bytesAddressPair = s.recvfrom(tamanho - HEADER_SIZE)
            message = bytesAddressPair[0]

            if message.decode('utf-8') == 'CRm0W>W?;GQ4AP.sSg':
                udp_open = False
            elif len(message.decode('utf-8')) != (tamanho - HEADER_SIZE):
                s.sendto(str.encode('ACK'), bytesAddressPair[1])
                f.write(message)
            else:
                is_ack, message_content = verify_checksum(message)
                if is_ack:
                    s.sendto(str.encode('ACK'), bytesAddressPair[1])
                    f.write(message_content)
                else:
                    print("NACK")
                    s.sendto(str.encode('NACK'), bytesAddressPair[1])

        f.close()
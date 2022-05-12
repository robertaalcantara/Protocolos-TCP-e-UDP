from TCP_server import TCP_server 

tamanhos = [100, 500, 1000]
HEADER_SIZE = 54

for tamanho in tamanhos:
    for i in range(10):
        tempo = TCP_server(tamanho, HEADER_SIZE)
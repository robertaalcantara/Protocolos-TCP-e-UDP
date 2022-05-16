from UDP_rdt_server import UDP_rdt_server 
import time

tamanhos = [100, 500, 1000]
HEADER_SIZE = 42

for tamanho in tamanhos:
    for i in range(10):
        UDP_rdt_server(tamanho, HEADER_SIZE)
        print(f"Finished iteration {i} for size {tamanho}")
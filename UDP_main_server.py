from UDP_server import UDP_server 
import time

tamanhos = [100, 500, 1000]
HEADER_SIZE = 54

for tamanho in tamanhos:
    UDP_server(tamanho, HEADER_SIZE)
    print(f"Finished iteration {i} for size {tamanho}")
    time.sleep(0.1)
from TCP_server import TCP_server 
import time

tamanhos = [100, 500, 1000]
HEADER_SIZE = 54

for tamanho in tamanhos:
    for i in range(10):
        TCP_server(tamanho, HEADER_SIZE, (i==9 and tamanho==1000))
        print(f"Finished iteration {i} for size {tamanho}")
        time.sleep(0.1)
    time.sleep(0.3)
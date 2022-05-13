from TCP_client import TCP_client 
import time
import pandas as pd

tamanhos = [100, 500, 1000]
HEADER_SIZE = 54
protocolo = 'TCP'

for tamanho in tamanhos:
    tempos = []
    sizes = []
    for i in range(10):
        time.sleep(0.5)
        tempo = TCP_client(tamanho, HEADER_SIZE)
        tempos.append(tempo)
        sizes.append(tamanho)
        print(f"Finished iteration {i} for size {tamanho}")
    time.sleep(0.5)

    results = pd.DataFrame({
            'Tamanho': sizes,
            'Tempos': tempos
        })
    if tamanho==100 and protocolo=='TCP':
        results.to_csv("Resultados.csv",index=False)
    else:
        file_df = pd.read_csv("Resultados.csv")
        file_df = pd.concat([file_df,results], ignore_index=True)
        file_df.to_csv("Resultados.csv",index=False)
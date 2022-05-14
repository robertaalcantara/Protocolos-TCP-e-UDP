from TCP_client import TCP_client 
import time
import pandas as pd

tamanhos = [100, 500, 1000]
HEADER_SIZE = 66

for tamanho in tamanhos:
    tempos = []
    sizes = []
    total_pacotes = []

    for i in range(10):
        time.sleep(1)
        tempo, contador_pacotes = TCP_client(tamanho, HEADER_SIZE)
        tempos.append(tempo)
        sizes.append(tamanho)
        total_pacotes.append(contador_pacotes)
        print(f"Finished iteration {i} for size {tamanho}, {tempo} seg")
    time.sleep(1)

    results = pd.DataFrame({
            'Tamanho': sizes,
            'Tempos': tempos,
            'Pacotes': total_pacotes
        })
    if tamanho==100:
        results.to_csv("ResultadosTCPPCPETEthernet.csv",index=False)
    else:
        file_df = pd.read_csv("ResultadosTCPPCPETEthernet.csv")
        file_df = pd.concat([file_df,results], ignore_index=True)
        file_df.to_csv("ResultadosTCPPCPETEthernet.csv",index=False)
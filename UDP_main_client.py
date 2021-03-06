from UDP_client import UDP_client, close_UDP
import time
import pandas as pd

tamanhos = [100, 500, 1000]
HEADER_SIZE = 42

for tamanho in tamanhos:
    tempos = []
    sizes = []
    total_pacotes = []

    for i in range(10):
        tempo, contador_pacotes = UDP_client(tamanho, HEADER_SIZE)
        time.sleep(1)
        close_UDP()
        tempos.append(tempo)
        sizes.append(tamanho)
        total_pacotes.append(contador_pacotes)
        print(f"Finished iteration {i} for size {tamanho}")
        time.sleep(2)

    results = pd.DataFrame({
            'Tamanho': sizes,
            'Tempos': tempos,
            'Pacotes': total_pacotes
        })
    if tamanho==100:
        results.to_csv("ResultadosUDPSemGarantiaPCPETEthernet.csv",index=False)
    else:
        file_df = pd.read_csv("ResultadosUDPSemGarantiaPCPETEthernet.csv")
        file_df = pd.concat([file_df,results], ignore_index=True)
        file_df.to_csv("ResultadosUDPSemGarantiaPCPETEthernet.csv",index=False)

    time.sleep(5)
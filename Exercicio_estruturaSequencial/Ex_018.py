"""Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos)."""
download = int(input("Insira o tamanho do arquivo que deseja baixar em Megabytes (MB): "))
velocidade = int(input("Insira a velocidade de download em Mbps: "))

megabites = velocidade * 0.125

tempo_download = download / megabites

minuto = tempo_download//60
resto = tempo_download%60

print(f"O tempo aproximado de download do arquivo de {download}MB em conjunto com a velocidade de {velocidade}Mbps é de {tempo_download:.3f} segundos ou {minuto:.0f}:{resto:.0f} minutos")
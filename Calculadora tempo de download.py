tamanhoarquivo = float(input("Qual o tamanho do arquivo em Mb "))
velocidade_de_internet = float(input("Qual a velocidade da internet em Mbps"))

velocidade_real = (velocidade_de_internet /8 )

tempo_download_segundos = (tamanhoarquivo / velocidade_real)
tempo_download_minutos = ((tamanhoarquivo / velocidade_real) / 60)

print ("o tempo de download em segundos é de:" , tempo_download_segundos)
print ("O tempo em minutos é de: %.2f " % (tempo_download_minutos))


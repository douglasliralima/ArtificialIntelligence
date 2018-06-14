import matplotlib.pyplot as plt
import datetime as dt
import time

#Bom, quando estamos trabalhando com unidades de tempo, pode ser meio complicado lidar com elas em nossa visualização dos dados
#vamos dar uma olhada nas bases de como fazer isso

#Existem padrões para contabilização de unidades de tempo, uma das mais antigas e mais famosas é a unix time
tempo_agora = time.time()
print("Tempo no formato Unix:", tempo_agora, sep = '\n')
print("Tempo legível graças a datetime:", dt.datetime.fromtimestamp(tempo_agora), sep = '\n')#Tempo legível

#------------------------NOT TODAY!-----------------------------------------------
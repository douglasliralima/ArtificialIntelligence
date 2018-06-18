import pandas as pd
import numpy as np
from socket import *
from Comunicacao import Comunicacao

serverSocket = "localhost"
portNumber = 50007
tradutor = Comunicacao()

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((serverSocket, portNumber))
sockobj.listen(5)

while True:

	conexao, endereco = sockobj.accept()
	print("Server conectado com", endereco)
	valor = tradutor.protocoloEntrada(conexao)
	print(valor)
	tradutor.protocoloSaida(conexao, valor)
	#conexao.send(valor.encode())
	count = 0
	conexao.close()
	print("Cliente desconectado")
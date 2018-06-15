import pandas as pd
import numpy as np
from socket import *

serverSocket = "localhost"
portNumber = 50007
dados = pd.read_csv('Monstros.csv')
nomes = dados['Name'].tolist()

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((serverSocket, portNumber))
sockobj.listen(5)

while True:

	conexao, endereco = sockobj.accept()
	print("Server conectado com", endereco)

	entrada = conexao.recv(1024)

	count1 = 0
	valor = ''
	for nome in nomes:
		if(nome == entrada):
			count2 = 0
			for atributo in dados:
				print(count2)
				valor += str(dados[atributo][count1])
				if(count2 < len(dados.keys()) - 1):
					valor += ','
				count2+=1
			break
		count1+=1

	conexao.send(data.encode())
	count = 0
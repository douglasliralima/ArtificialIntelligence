import pandas as pd
import numpy as np
from socket import *
from Comunicacao import Comunicacao
from Projeto import Projeto

serverSocket = "localhost"
portNumber = 50008
tradutor = Comunicacao()
ia = Projeto()

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((serverSocket, portNumber))
sockobj.listen(5)

while True:

	conexao, endereco = sockobj.accept()
	print("Server conectado com", endereco)
	acao = int(conexao.recv(1).decode()) #Pego o sinal do que é preciso ser feito, 1 - para busca de monstros, 2 - Determinar pela IA
	if(acao == 1):
		print("Procura de monstros")
		monstro = tradutor.protocoloEntrada(conexao, acao)
		print(monstro)
		tradutor.protocoloSaida(conexao, monstro)
		
	elif(acao == 2):
		print("Determinacao de monstros")
		atributos = tradutor.protocoloEntrada(conexao, acao)
		ia.setMonsterIn(atributos[0], atributos[1], atributos[2], atributos[3], atributos[4], atributos[5])
		monstro = ia.getMonsterOut()
		print(monstro)
		tradutor.protocoloSaida(conexao, monstro)

	conexao.close()
	print("Cliente desconectado")
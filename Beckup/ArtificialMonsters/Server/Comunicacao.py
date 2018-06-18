from socket import *
import pandas as pd

class Comunicacao:

	def __init__(self):	
		self.dados = pd.read_csv('Monstros.csv')
		self.nomes = self.dados['Name'].tolist()

	def _procuraMonstro(self, entrada):
		valor = ""
		count1 = 0
		for nome in self.nomes:
			if(nome == entrada):
				count2 = 0
				for atributo in self.dados:
					valor += str(self.dados[atributo][count1])
					if(count2 < len(self.dados.keys()) - 1):
						valor += ','
					count2+=1
				break
			count1+=1
		return valor

	def protocoloEntrada(self, cliente):
		conexao = cliente
		entrada = ''
		while(True):
			#Recebe do cliente
			aux = conexao.recv(1)
			if(aux.decode() == ';'): #Sinal que a comunicação acabou
				break
			#Salva o que o cliente mandou e pede para ele enviar o resto
			entrada += aux.decode()
			conexao.send('c'.encode())
		monstro = self._procuraMonstro(entrada)
		return monstro
		
	def protocoloSaida(self, cliente, monstro):
		conexao = cliente
		for i in range(len(monstro)):
			cliente.send(monstro[i].encode()) #Manda para o cliente cada byte de caracter da string
			#Vê se pode continuar mandando
		cliente.send(';'.encode()) #Sinal para o cliente de que tudo foi mandado


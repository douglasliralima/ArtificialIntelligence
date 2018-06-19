from socket import *
import pandas as pd
import random

class Comunicacao:

	def __init__(self):	
		self.dados = pd.read_csv('Monstros.csv')
		self.nomes = self.dados['Name'].tolist()

		'''

                i = 1
                print("Hit Dice:", artificialMonster['Hit dice'])
                # Faz um while que cálcula cada rolagem de dados para vida:
                while (i <= artificialMonster['Hit dice']):
                    # Simula à rolagem de um dado fazendo um random integer que vai
                    # de 1 até o número máximo do dado especificado pela variável dice
                    hitPoints += random.randint(1, dice)

                    i += 1
                print("Hit Points (antes do Life Bonus):", hitPoints)
                print("Life Bonus:", lifeBonus)
                hitPoints += lifeBonus
                print("Hit Points:", hitPoints)
		'''

	def _procuraMonstro(self, entrada):
		#Guardar os valores do 6 ao 8
		valor = ""
		count1 = 0
		hitPoints = 0
		for nome in self.nomes:
			if(nome == entrada):
				count2 = 0
				for atributo in self.dados:
					print(atributo)
					if(atributo == "Armor Class"):
						print("Entrou armor class")
						ArmorGeral = self.dados['Armor Class'][count1] + '|'
						count3 = 0 
						aux = ""
						ca_normal = 0
						ca_touch = 0
						ca_surprise = 0
						for letra in ArmorGeral:
							if(letra == '|'):
								if(count3 == 0):
									ca_normal = int(aux)
								elif(count3 == 1):
									ca_touch = int(aux)
								elif(count3 == 2):
									ca_surprise = int(aux)
								aux = ""
								count3 +=1
								continue
							aux += letra
						#print("ca normal", ca_normal, ca_touch, ca_surprise)

						if(self.dados['Syze'][count1] == "Colossal"):
							armorSizeModifier = -4

						elif(self.dados['Syze'][count1] == "Gargantuan"):
							armorSizeModifier = -3

						elif(self.dados['Syze'][count1] == "Huge"):
							armorSizeModifier = -2

						elif(self.dados['Syze'][count1] == "Large"):
							armorSizeModifier = -1

						elif(self.dados['Syze'][count1] == "Medium"):
							armorSizeModifier = 0

						elif(self.dados['Syze'][count1] == "Small"):
							armorSizeModifier = 1

						elif(self.dados['Syze'][count1] == "Tiny"):
							armorSizeModifier = 2

						elif(self.dados['Syze'][count1] == "Diminutive"):
							armorSizeModifier = 3

						elif(self.dados['Syze'][count1] == "Fine"):
							armorSizeModifier = 4

						mod_dex = ca_touch - armorSizeModifier - 10
						dex = (mod_dex * 2) + 10

						natural_armor = ca_surprise - armorSizeModifier - 10
						valor += str(natural_armor) + "," + str(armorSizeModifier) + ","
						count2+=1
						continue


					elif(atributo == 'Hit dice'):
						print("Entrou hit dice")
						dice = self.dados['Dice Type'][count1]
						dice = int(dice[1:])
						hitdice = int(self.dados['Hit dice'][count1])
						#print(hitdice)
						i = 1
						while(i <= hitdice):
							hitPoints += random.randint(1,dice)
							i+=1
						hitPoints += int(self.dados['Life Bonus'][count1])
						valor += str(hitPoints) + ","
						#print(valor)
						count2+=1
						continue

					elif(atributo == 'Dice Type' or atributo == 'Life Bonus'):
						print("Entrou Dice type ou life bonus")
						count2+=1
						continue
					else:
						print("Entrou normal")
						valor += str(self.dados[atributo][count1])
						if(count2 < len(self.dados.keys()) - 1):
							valor += ','
						count2+=1
			count1+=1
		return valor
		
		'''
		Retorna tudo no formato: Indice no dataframe, Nome do Monstro, Tipo, Subtipo, Tamanho, Hit Points,
		iniciativa, speed, armadura natural, modificador especial de tamanho (CA outros),
		Ataque, Ataque Total, Espaço|Alcance, Ataques Especiais, Qualidades Especiais,
		Fortitude, Reflexes, Will, Str, Dex, Con, Int, Wis, Cha, Skill, Feats, Environment,
		ND(Volta em float), Treasure, Alignement, Lvl Adjustment, Advancement

		'''

	def _separaAtributos(self,entrada):
		atributos = []
		atributo = ""
		entrada += ','
		for i in range(len(entrada)):
			if(entrada[i] != ','):
				atributo += entrada[i]
			else:
				atributos.append(atributo)
				atributo = ""
		return atributos



	def protocoloEntrada(self, cliente, acao):
		conexao = cliente #Recebe o cliente
		entrada = ''
		while(True):
			#Recebe do cliente
			aux = conexao.recv(1)
			if(aux.decode() == ';'): #Sinal que a comunicação acabou
				break
			#Salva o que o cliente mandou e pede para ele enviar o resto
			entrada += aux.decode()
			conexao.send('c'.encode())
			
		if(acao == 1):
			return self._procuraMonstro(entrada)

		elif(acao == 2):
			return self._separaAtributos(entrada)
		
	def protocoloSaida(self, cliente, monstro):
		conexao = cliente
		for i in range(len(monstro)):
			cliente.send(monstro[i].encode()) #Manda para o cliente cada byte de caracter da string
			#Vê se pode continuar mandando
		cliente.send(';'.encode()) #Sinal para o cliente de que tudo foi mandado


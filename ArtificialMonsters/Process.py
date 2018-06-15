import pandas as pd
import numpy as np


class Process:
'''
Fazer um dicionário de dicionários, onde cada coluna seja referenciavel pelo atributo
cada elemento desse dicionario sera a relação do numero naquele atributo e o seu string correspondente
vamos chamar isso de bigDic
'''

#A funcao pega todas as colunas que foram passadas no dataframe e discretiza os seus valores
#retornando um dataframe com os valores discretizadostransformacoes = {}
__traducaoUsuario = {} #Grande dicionario de dicionarios que guarda cada uma de nossas strings e sua correlações númericas em um dataframe ficticio
__traducaoPrograma = {}

	def __discretiza(colunas):
		#Lembrando que ao recebermos um dicionário no for, ele vai printando suas palavras chave, então basta que
		#a cada palavra chave no for, nós percorramos toda a linha
		novasColunas = {}

		for instancia in colunas:
			palavras = []  #Representará cada um dos nossos rótulos
			valores = {}   #Representará cada um dos valores númericos referentes a esses rótulos
			valor = 0      #O número subirá a partir disso
			rotulados = [] #Representacao de cada elemento classificado, com um rótulo numérico

			for elemento in colunas[instancia]:
				'''
				Vou ver em uma lista se eu já não me deparei com esse
				mesmo elemento anteriomente nessa coluna
				'''
				existe = False

				for x in range(len(palavras)):
					if(len(palavras) == 0):
						#Se não existia nenhum elemento anteriormente, obviamente não havia nada antes para estar igual
						existe = True
						break
					#Se eu encontrar um único elemento igual, eu retiro ela da minha lista
					if(palavras[x] == elemento):
						existe = True
						palavras.remove(elemento)
						#print("Dropei", elemento, end = "")
						break
				palavras.append(elemento)

				#Bom, se o elemento não existir na minha lista, eu o adiciono no meu dicionário de valores
				if(existe == False):
					#print("Elemento:", elemento, "Valor:", valor)
					valores[elemento] = valor
					valor +=1
				#Para cada instancia nessa coluna vamos pegar o valor correspondente do elemento, 
				#em nosso dicionario de valores
				rotulados.append(valores[elemento])

			#Guardamos a referência do que foi traduzido para ser usado em nossa entrada
			Process.__traducaoUsuario[instancia] = valores
			#Em nossa saída, a única coisa que precisamos guardar a tradução é para dado número chegar na string de Armor Class
			if(instancia == 'Armor Class'):
				Process.__traducaoPrograma = {y:x for x,y in valores.items()} #Metodo para trocar os chaves pelos valores de um dicionario
				
			#Agora seguindo o formato do pandas, eu deixo a palavra chave daquela coluna, para a lista de rotulados
			novasColunas[instancia] = rotulados
		#Retornamos o dataframe convertido
		#print(Process.__traducaoPrograma.head())
		return pd.DataFrame.from_dict(novasColunas) #Construir um dataframe a partir de um dicionario



	#Vamos tratar os casos de um atributo neutro, que no caso é retratado no dataset como o '-'
	def __atributoNeutro(df):
		#Lembrando que ao recebermos um dicionário no for, ele vai printando suas palavras chave, então basta que
		#a cada palavra chave no for, nós percorramos toda a linha
		new_df = pd.DataFrame(df)
		#print(new_df['LvL Adjustment'].tail())
		for instancia in new_df:
			i = 0
			#Vamos percorrer essa lista
			aux = new_df[instancia].tolist() #Nos temos Series em nossas palavras chaves, elas são como listas, só que com outros metodos
			for elemento in aux:
				if(elemento == "-"):
					del(aux[i])
					#Como todos os elementos são strings que serão convertidas para inteiros, colocamos ele como string tbm
					aux.insert(i, '-1')
				i+=1
				new_df[instancia] = aux
		#print(new_df['LvL Adjustment'].tail())
		return new_df



	def __badMonsters(df):
		#print(df)
		df.drop(205, inplace = True)
		return pd.DataFrame(df)



	def preprocessMonster(monstros):
		monstros = monstros.drop(['Name', 'ID', 'Sub-Type', 'Attack', 'Full Attack', 'Special Attacks',
		 'Special Qualities', 'Skills', 'Feats', 'Organization', 'Advancement', 'Dice Type', 'Life Bonus',
		  'Dex', 'Initiative', 'Base Attack', 'Speed', 'Grapple', 'Space|Reach', 'Treasure'],
		axis = 1)#Essas colunas eram todas inúteis para a nossa discretização
		

		dados_nreais =  monstros.drop(['Type', 'Syze', 'Armor Class', 'Enviroments', 'Alignment'], axis = 1)
		#print(dados_nreais.head())
		dados_naonumericos = monstros[['Type', 'Syze', 'Armor Class', 'Enviroments', 'Alignment']]
		#print(dados_naonumericos.head())

		dados_ndiscretos = __discretiza(dados_naonumericos)
		print(dados_ndiscretos.head())

		#No caso axis é a coordanada que vamos ir concatenando, se fosse linhas era 0, mas como é colunas ele é 1
		#sorted = false, significa que é para ele colocar na sequência em que isso foi concatenado
		dados_normalizados = pd.concat([dados_nreais, dados_ndiscretos], axis=1)
		#print(dados_normalizados.head())

		neutro_processado = __atributoNeutro(dados_normalizados)

		dados_processados = __badMonsters(neutro_processado)
		#print(dados_processados)
		return dados_processados

		
	def traduzUsuario(monstro):
		monstro_programa = {}
		#print(Process.__traducaoUsuario)
		for atributo in monstro:
			for elemento in monstro[atributo]:
				monstro_programa[atributo] = Process.__traducaoUsuario[atributo][elemento]

		aux = pd.DataFrame(monstro_programa, index=[0])
		return pd.DataFrame.from_dict(aux)

	
	#Esse método pega o valor processado do programa pelo multipredict e o reconfigura da mesma maneira do que foi passado para ele
	def protocoloSaida(y, entrada):
		monstro_programa = {}
		count = 0
		for atributo in y:
			if(atributo == 'Armor Class'):
				for elemento_saida in Process.__traducaoPrograma:
					monstro_programa[atributo] = Process.__traducaoPrograma[entrada[count]]
			else:
				monstro_programa[atributo] = entrada[count]
			count+=1
		return monstro_programa
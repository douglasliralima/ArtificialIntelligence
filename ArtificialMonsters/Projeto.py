import pandas as pd
import numpy as np
import math
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPRegressor
from sklearn import svm
from sklearn.decomposition import PCA
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
#from sklearn.multioutput import RegressorChain
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.tree import ExtraTreeRegressor
from sklearn.svm import LinearSVR
from sklearn.svm import LinearSVC
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import RandomForestRegressor
from collections import OrderedDict
from sklearn.multioutput import MultiOutputClassifier
import collections

'''
Fazer um dicionário de dicionários, onde cada coluna seja referenciavel pelo atributo
cada elemento desse dicionario sera a relação do numero naquele atributo e o seu string correspondente
vamos chamar isso de bigDic
'''

#A funcao pega todas as colunas que foram passadas no dataframe e discretiza os seus valores
#retornando um dataframe com os valores discretizadostransformacoes = {}
traducaoUsuario = {} #Grande dicionario de dicionarios que guarda cada uma de nossas strings e sua correlações númericas em um dataframe ficticio
traducaoPrograma = {}

def discretiza(colunas):
	#Lembrando que ao recebermos um dicionário no for, ele vai printando suas palavras chave, então basta que
	#a cada palavra chave no for, nós percorramos toda a linha
	novasColunas = {}
	global traducaoUsuario
	global traducaoPrograma

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
		traducaoUsuario[instancia] = valores
		#Em nossa saída, a única coisa que precisamos guardar a tradução é para dado número chegar na string de Armor Class
		if(instancia == 'Armor Class'):
			traducaoPrograma = {y:x for x,y in valores.items()} #Metodo para trocar os chaves pelos valores de um dicionario
			
		#Agora seguindo o formato do pandas, eu deixo a palavra chave daquela coluna, para a lista de rotulados
		novasColunas[instancia] = rotulados
	#Retornamos o dataframe convertido
	#print(traducaoPrograma.head())
	return pd.DataFrame.from_dict(novasColunas) #Construir um dataframe a partir de um dicionario



def traduzUsuario(monstro):
	monstro_programa = {}
	global traducaoUsuario
	#print(traducaoUsuario)
	for atributo in monstro:
		for elemento in monstro[atributo]:
			monstro_programa[atributo] = traducaoUsuario[atributo][elemento]

	aux = pd.DataFrame(monstro_programa, index=[0])
	return pd.DataFrame.from_dict(aux)


def protocoloSaida(y, entrada):
	monstro_programa = {}
	count = 0
	for atributo in y:
		if(atributo == 'Armor Class'):
			for elemento_saida in traducaoPrograma:
				monstro_programa[atributo] = traducaoPrograma[entrada[count]]
		else:
			monstro_programa[atributo] = entrada[count]
		count+=1
	return monstro_programa

#Vamos tratar os casos de um atributo neutro, que no caso é retratado no dataset como o '-'
def atributoNeutro(df):
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



def badMonsters(df):
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

	dados_ndiscretos = discretiza(dados_naonumericos)
	print(dados_ndiscretos.head())

	#No caso axis é a coordanada que vamos ir concatenando, se fosse linhas era 0, mas como é colunas ele é 1
	#sorted = false, significa que é para ele colocar na sequência em que isso foi concatenado
	dados_normalizados = pd.concat([dados_nreais, dados_ndiscretos], axis=1)
	#print(dados_normalizados.head())

	neutro_processado = atributoNeutro(dados_normalizados)

	dados_processados = badMonsters(neutro_processado)
	#print(dados_processados)
	return dados_processados



    #----------------------------main----------------------------------------------------------------------------------
#Primeira coisa que fazemos é carregar o nosso dataset em um objeto da classe DataFrame
#Ele basicamente carrega o arquivo e coloca numa variável
dados = pd.read_csv('Monstros.csv')


dados = preprocessMonster(dados)

for i in dados.keys().values:
	print(i)

#print(dados.head())


x_train = dados.drop(['Hit dice', 'Armor Class', 'Fortitude', 'Reflexes', 'Will', 'Str', 'Con', 'Int', 'Wis', 'Cha'], axis = 1)
y_train = dados.drop(['Type', 'Syze', 'Enviroments', 'Alignment', 'LvL Adjustment', 'Challenge Rating'], axis = 1)

'''
tree1 = DecisionTreeClassifier(random_state = 4)
tree1.fit(x_train, y_train)
accuracyTree = tree1.score(x_test, y_test)

print('Acuracia da Arvore de classificação:',accuracyTree)
'''

tree = DecisionTreeRegressor(random_state = 4)
tree.fit(x_train, y_train)
#accuracyTree = tree.score(x_test, y_test)

#print('Acuracia da Arvore de decisão:',accuracyTree)


tree = DecisionTreeRegressor(random_state = 4)
tree.fit(x_train, y_train)
#accuracyTree = tree.score(x_test, y_test)

#print('Acuracia da Arvore de decisão:',accuracyTree)


regr_4 = RandomForestRegressor()
regr_4.fit(x_train, y_train)
#acuracia1 = regr_4.score(x_test, y_test)
#print("Acuracia da RandomForestRegressor:", acuracia1)

regr_5 = ExtraTreesRegressor()
regr_5.fit(x_train, y_train)
#acuracia2 = regr_5.score(x_test, y_test)
#print("Acuracia das Arvores de regreção:", acuracia2)

regr_3 = ExtraTreeRegressor()
regr_3.fit(x_train, y_train)
#acuracia2 = regr_3.score(x_test, y_test)
#print("Acuracia da Arvore de regreção:", acuracia2)


'''
knn = KNeighborsRegressor()
knn.fit(x_train, y_train)
accuracyKnn = knn.score(x_test, y_test)

print('Acuracia do KNN:',accuracyKnn)
'''

new_data = OrderedDict([
        ('Type', 'Magical Beast'),
        ('Syze', 'Large'),
        ('Enviroments', 'Desert Warn'),
        ('Alignment', 'Chaotic Good'),
        ('LvL Adjustment', '5'),
        ('Challenge Rating', '9')
        ])

#print(new_data)

aux = pd.DataFrame(new_data, columns=new_data.keys(), index = [0])
new_data_naonumeros = aux[['Type', 'Syze', 'Enviroments', 'Alignment']]
new_data_numeros = aux.drop(['Type', 'Syze', 'Enviroments', 'Alignment'], axis = 1 )

new_data_naonumeros = traduzUsuario(new_data_naonumeros)
#print(new_data_naonumeros, new_data_numeros, sep = '\n')

aux = pd.concat([new_data_numeros, new_data_naonumeros], axis=1)
#print(aux)

monstro = {}
for atributo in aux:
	for elemento in aux[atributo]:
		monstro[atributo] = elemento

monstro_usuario = OrderedDict(sorted(monstro.items(), key=lambda t: len(t[0])))

monstro = pd.Series(monstro_usuario).values.reshape(1,-1)

predict1 = tree.predict(monstro)
predict2 = regr_4.predict(monstro)
predict3 = regr_3.predict(monstro)
predict4 = regr_5.predict(monstro)

numeros = predict1[0 , :]
resultado1 = [int(x) for x in numeros]

numeros = predict2[0 , :]
resultado2 = [int(x) for x in numeros]

numeros = predict3[0 , :]
resultado3 = [int(x) for x in numeros]

numeros = predict4[0, :]
resultado4 = [int(x) for x in numeros]

print("\n" * 2, "Resultado 1:", resultado1, sep = "\n")
print(protocoloSaida(y_train, resultado1))
print("\n" * 2, "Resultado 2:", resultado2, sep = "\n")
print(protocoloSaida(y_train, resultado2))
print("\n" * 2, "Resultado 3:", resultado3, sep = "\n")
print(protocoloSaida(y_train, resultado3))
print("\n" * 2, "Resultado 4:", resultado4, sep = "\n")
print(protocoloSaida(y_train, resultado4))




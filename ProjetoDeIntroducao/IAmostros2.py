#Estamos criando um objeto diretamente das bibliotecas 
import pandas as pd
import numpy as np
import math

'''
Pegamos aqui classes da biblioteca mãe especificamente para podermos usar
'''
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split #Para fazer os testes
#Importamos aqui o regressor
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPRegressor
from sklearn import svm
from sklearn.decomposition import PCA
from sklearn.metrics import r2_score
from sklearn.svm import SVC



#A funcao pega todas as colunas que foram passadas no dataframe e discretiza os seus valores
#retornando um dataframe com os valores discretizados
def discretiza(colunas):
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
		#Agora seguindo o formato do pandas, eu deixo a palavra chave daquela coluna, para a lista de rotulados
		novasColunas[instancia] = rotulados
	#Retornamos o dataframe convertido
	return pd.DataFrame.from_dict(novasColunas) #Construir um dataframe a partir de um dicionario




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
				aux.insert(i, '10000')
			i+=1
			new_df[instancia] = aux
	#print(new_df['LvL Adjustment'].tail())
	return new_df



def badMonsters(df):
	#print(df)
	df.drop(205, inplace = True)
	return pd.DataFrame(df)




def preprocessMonster(monstros):
	monstros = monstros.drop(['Name', 'ID', 'Sub-Type', 'Attack', 'Full Attack', 'Special Attacks', 'Special Qualities', 'Skills', 'Feats', 'Organization', 'Advancement'],
	axis = 1)#Essas colunas eram todas inúteis para a nossa discretização

	dados_nreais =  monstros.drop(['Type', 'Syze', 'Dice Type', 'Speed', 'Armor Class',  'Space|Reach', 'Enviroments', 'Treasure', 'Alignment'], axis = 1)
	#print(dados_nreais.head())
	dados_naonumericos = monstros[['Type', 'Syze', 'Dice Type', 'Speed', 'Armor Class',  'Space|Reach', 'Enviroments', 'Treasure', 'Alignment']]
	#print(dados_naonumericos.head())

	dados_ndiscretos = discretiza(dados_naonumericos)
	#print(dados_ndiscretos.head())

	#No caso axis é a coordanada que vamos ir concatenando, se fosse linhas era 0, mas como é colunas ele é 1
	#sorted = false, significa que é para ele colocar na sequência em que isso foi concatenado
	dados_normalizados = pd.concat([dados_nreais, dados_ndiscretos], axis=1, sort=False)
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

#print(dados)


x = dados.drop(['LvL Adjustment'], axis = 1)
y = dados['LvL Adjustment']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 2)

for i in range(5):
	print("teste nº", i, sep = "")
	knn = KNeighborsClassifier()
	knn.fit(x_train, y_train)

	acuracia = knn.score(x_test, y_test)
	print("Acuracia do KNN:", acuracia)

	#------------------

	svm = SVC()
	svm.fit(x_train, y_train)

	acuracia1 = svm.score(x_test, y_test)
	print("Acuracia do SVM:", acuracia1)


	#------------------

	arvore = DecisionTreeClassifier()
	arvore.fit(x_train, y_train)

	acuracia2 = arvore.score(x_test, y_test)
	print("Acuracia da arvore:", acuracia2)

	print("\n" * 3)

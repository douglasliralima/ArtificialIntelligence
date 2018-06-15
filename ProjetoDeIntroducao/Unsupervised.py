import pandas as pd
import numpy as np
import math
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import MeanShift
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


#from sklearn.multioutput import RegressorChain

'''
OBJETIVO:
Image que o mestre criou um monstro qualquer da mente dele, settando todas as suas respectivas instâncias
o que nós vamos fazer aqui é procurar alguma estrutura em nossos monstros onde, a partir daquilo que o mestre entregue
para a IA, ela encontre mais ou menos qual seria o Challange Rate dele
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
		if(instancia == 'Syze'):
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


#Pegamos aqui os nossos atributos em x e os valores do centroide previstos
def protocoloSaida(x, yc):
	monstro_programa = {}
	count = 0
	for atributo in x:
		if(atributo == 'Syze'):
			for elemento_saida in yc:
				monstro_programa[atributo] = traducaoPrograma[yc[count]]
		else:
			monstro_programa[atributo] = yc[count]
		count+=1
	return monstro_programa

'''
Receberemos vários elementos, vamos procurar se aquele elemento faz parte do grupo que queremos formar um
dataframe, se ele fizer, o dicionario recebe ele como instância, adicionando cada um de seus atributos correspondentes
'''
def retransformaGrupo(elementos, localizacoes, numero_centros, atributos, nGrupo):
	grupos = []
	grupo = []
	for i in range(numero_centros):
		count1 = 0
		for j in localizacoes:
			if(j == i):
				if(j == nGrupo): #Vamos pegar o grupo que queremos retornar
					grupo.append(elementos[count1].astype(int))
				grupos.append(elementos[count1].astype(int)) #Para visualizar os grupos
			count1+=1
		monstros = pd.DataFrame(data = grupos, columns = atributos)
		grupos = []
	return pd.DataFrame(data = grupo, columns = atributos)


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
	monstros = monstros.drop(['Name', 'ID', 'Sub-Type', 'Attack', 'Full Attack', 'Special Attacks', 'Special Qualities',
	 'Skills', 'Feats', 'Organization', 'Advancement', 'Dice Type', 'Life Bonus', 'Dex', 'Initiative', 'Base Attack',
	 'Speed', 'Grapple', 'Space|Reach', 'Treasure',
	 'Type',  'Enviroments', 'Alignment'],
	axis = 1)#Essas colunas eram todas inúteis para a nossa discretização

	dados_nreais =  monstros.drop([#'Type', 'Enviroments', 'Alignment',
	 'Armor Class','Syze'], axis = 1)
	#print(dados_nreais.head())
	dados_naonumericos = monstros[[#'Type',  'Enviroments', 'Alignment',
	 'Armor Class','Syze']]
	#print(dados_naonumericos.head())

	dados_ndiscretos = discretiza(dados_naonumericos)
	#print(dados_ndiscretos.head())

	#No caso axis é a coordanada que vamos ir concatenando, se fosse linhas era 0, mas como é colunas ele é 1
	#sorted = false, significa que é para ele colocar na sequência em que isso foi concatenado
	dados_normalizados = pd.concat([dados_nreais, dados_ndiscretos], axis=1)
	#print(dados_normalizados.head())

	neutro_processado = atributoNeutro(dados_normalizados)

	dados_processados = badMonsters(neutro_processado)
	#print(dados_processados)
	return dados_processados

def elementoGrupo(localizacoes, n_centros):

	count = []
	for i in range(n_centros):
		count.append(0)

	aux = 0
	for j in range(n_centros):
		for i in localizacoes:
			if(i==j):
				aux += 1
				count[j] = aux
		aux = 0
	return count

    #----------------------------main----------------------------------------------------------------------------------
#Primeira coisa que fazemos é carregar o nosso dataset em um objeto da classe DataFrame
#Ele basicamente carrega o arquivo e coloca numa variável
dados = pd.read_csv('Monstros.csv')


dados = preprocessMonster(dados)


#Nos transformamos tudo em float e pegamos os arrays dessas merd4s, o primeiro elemento é a linha e o segundo a coluna, matriz 2D
y_train = np.array(dados['Challenge Rating'])
x_train = dados.drop(['Armor Class', 'LvL Adjustment', 'Syze'], axis = 1).astype(float).values#Damos todos os dados para treinar nossa IA, menos a coluna que tem as respostas
print(x_train)
atributos = dados.drop(['Armor Class', 'LvL Adjustment', 'Syze'], axis = 1).keys().values
#Pegamos apenas as respostas que sabemos como corretas

#Acho que assim como a Thais falou, o melhor aqui é primeiro encontrar grupos pelo hierarquico e depois jogar
#esse número de grupos no k means


ms = MeanShift()
ms.fit(x_train)
localizacoes = ms.labels_ #pegamos o array com as respectivas localizações de cada elemento em nossos grupos
#O método do numpy unique filtra apenas os dados que são únicos no array passado e põe em outro array
n_centros = len(np.unique(localizacoes)) #Logo podemos assim pegar o número de centros
print("Total de", n_centros, "\n" * 2)
print(localizacoes)
for i in range(len(ms.cluster_centers_)):
	print(protocoloSaida(atributos, ms.cluster_centers_[i].astype(int)), '\n')

print(elementoGrupo(localizacoes, n_centros))
#Com base nisso, podemos ver que os grupos de 2 a 9 são outliers em nossa base de dados, por formarem grupos com pouquissísmos elementos
#Todos eles totalizam 13 instâncias, como não é uma perda tão grande, vamos fazer um outro objeto numpy com base neles e processa-lo novamente
count = 0
new_ds = []
for i in localizacoes:
	if(i == 0):
		new_ds.append(x_train[count])
		count+=1
	elif(i == 1):
		new_ds.append(x_train[count])
		count+=1
	elif(i == 3):
		new_ds.append(x_train[count])
		count+=1
	elif(i == 9):
		new_ds.append(x_train[count])
		count+=1

	elif(i==10):
		new_ds.append(x_train[count])
		count+=1
	else:
		count+=1
		continue


clf = KMeans(n_clusters=3)
clf.fit(new_ds)
localizacoes = clf.labels_ 
n_centros = len(np.unique(localizacoes))
print("Total de", n_centros, "\n" * 2)
print(localizacoes)
for i in range(len(clf.cluster_centers_)):
	print(protocoloSaida(atributos, clf.cluster_centers_[i].astype(int)), '\n')

print(elementoGrupo(localizacoes, n_centros))

#Vamos agora testar a acurâcia para cada um desses grupos
for i in range(3):
	grupo_monstros = retransformaGrupo(new_ds, localizacoes, n_centros, atributos, i)
	#print(grupo_monstros.head())
	print('\n' * 2, i)

	x = grupo_monstros.drop(['Challenge Rating'], axis = 1)
	y = grupo_monstros['Challenge Rating']
	#x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.1, random_state = 1)

	knn = KNeighborsRegressor(n_neighbors = 3)
	knn.fit(x, y)

	acuracia = cross_val_score(knn, x, y, cv=8)
	print("Knn acuracia:", acuracia.mean())

	tree = DecisionTreeRegressor(criterion = 'mae', min_samples_split = 6,  min_samples_leaf = 4)
	tree.fit(x,y)

	acuracia = cross_val_score(tree, x, y, cv=5)
	print("Arvore de decisao acuracia:", acuracia.mean())

	svm = SVR(kernel = 'linear')
	svm.fit(x,y)

	acuracia = cross_val_score(svm, x, y, cv=5)
	print("SVM acuracia:", acuracia.mean())

	lr = LinearRegression(fit_intercept = False, copy_X = False)
	lr.fit(x,y)

	acuracia = cross_val_score(lr, x, y, cv=5)
	print("Linear Regression acuracia:", acuracia.mean())

	rf = RandomForestRegressor(criterion = 'mae', max_features = 'log2', n_estimators = 15, warm_start = True)
	rf.fit(x,y)

	acuracia = cross_val_score(rf, x, y, cv=5)
	print("Random Forest acuracia:", acuracia.mean())
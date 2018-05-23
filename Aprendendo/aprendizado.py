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

#----------------------------main----------------------------------------------------------------------------------
#Primeira coisa que fazemos é carregar o nosso dataset em um objeto da classe DataFrame
#Ele basicamente carrega o arquivo e coloca numa variável
dados = pd.read_csv('Monstros.csv')

#Essa linha aqui rodava no dataset do armando, aqui usando o método do numpy is finite, eu estou removendo todas as instâncias do meu objeto
#que não possuem instanciado a variável year
#dados = df[np.isfinite(df['year'])]

#Nós podemos montar a seleção do que nós queremos em nosso DataFrame
#df = df[['Name', 'Type', 'Syze', 'Hit dice', 'Dice Type', 'Life Bonus', 'Initiative', 'Speed', 'Armor Class', 'Base Attack',
#		'Grapple', 'Space|Reach', 'Fortitude', 'Reflexes', 'will']]

#Ou então apenas dropar aquilo que não desejamos com o método drop

dados = dados.drop(['ID', 'Sub-Type', 'Attack', 'Full Attack', 'Special Attacks', 'Special Qualities', 'Skills', 'Feats', 'Organization', 'Advancement'],
	axis = 1)

dados = discretiza(dados)
print(dados)

'''
teste = {}
print(type(teste))

x = dados.drop(['LvL Adjustment'], axis = 1)
y = dados['LvL Adjustment']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 2)
knn = KNeighborsClassifier()
knn.fit(x_train, y_train)

acuracia = knn.score(x_test, y_test)
print("Acuracia:", acuracia)


#------------------

svm = SVC()
svm.fit(x_train, y_train)

acuracia1 = svm.score(x_test, y_test)
print("Acuracia:", acuracia1)


#------------------

arvore = DecisionTreeClassifier()
arvore.fit(x_train, y_train)

acuracia2 = arvore.score(x_test, y_test)
print("Acuracia:", acuracia2)'''
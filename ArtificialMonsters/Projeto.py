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
import Process



    #----------------------------main----------------------------------------------------------------------------------
#Primeira coisa que fazemos é carregar o nosso dataset em um objeto da classe DataFrame
#Ele basicamente carrega o arquivo e coloca numa variável
dados = pd.read_csv('Monstros.csv')


dados = Process.preprocessMonster(dados)

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

new_data_naonumeros = Process.traduzUsuario(new_data_naonumeros)
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
print(Process.protocoloSaida(y_train, resultado1))
print("\n" * 2, "Resultado 2:", resultado2, sep = "\n")
print(Process.protocoloSaida(y_train, resultado2))
print("\n" * 2, "Resultado 3:", resultado3, sep = "\n")
print(Process.protocoloSaida(y_train, resultado3))
print("\n" * 2, "Resultado 4:", resultado4, sep = "\n")
print(Process.protocoloSaida(y_train, resultado4))




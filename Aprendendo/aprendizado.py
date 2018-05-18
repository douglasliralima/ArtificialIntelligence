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
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPRegressor
from sklearn import svm
from sklearn.decomposition import PCA
from sklearn.metrics import r2_score

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

#print(dados.head()) #Veja, já é criado um ID automáticamente pelo negócio

teste = {}
print(type(teste))
'''
x = dados.drop(['Type'], axis = 1)
y = dados['Type']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 2)

knn = KNeighborsClassifier()
knn.fit(x_train, y_train)
acuracia = knn.score(x_test, y_test)
print("Acuracia:", acuracia)
'''
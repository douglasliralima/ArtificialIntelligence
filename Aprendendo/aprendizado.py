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

def handle_non_numerical_data(df):
    colunas = df.columns.values 		#Primeira coisa que nós vamos fazer é pegar o identificador de cada coluna, para transformar cada uma dela em valores numerais
    for coluna in colunas: 				#Vamos pegar o valor de cada coluna
        text_digit_vals = {}			#Criamos um dicionário que colocaremos os valores para cada coluna sistematizada
        def convert_to_int(val):		#Aqui nós pegamos uma palavra chave
            return text_digit_vals[val]	#retornamos então a coluna no dicionário com a coluna sistematizada caso o sistema precise
        if df[coluna].dtype != np.int64 and df[coluna].dtype != np.float64:#Vemos se o valor naquela respectiva coluna 
            column_contents = df[coluna].values.tolist()
            unique_elements = set(column_contents)
            x = 0
            for unique in unique_elements:
                if unique not in text_digit_vals:
                    text_digit_vals[unique] = x
                    x+=1

            df[coluna] = list(map(convert_to_int, df[coluna]))

    return df

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

dados = handle_non_numerical_data(dados)

print(dados.head()) #Veja, já é criado um ID automáticamente pelo negócio

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
print("Acuracia:", acuracia2)
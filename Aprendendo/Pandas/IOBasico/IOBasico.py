'''Geralmente, para abrir certos formatos de arquivo, como csv, HTML, XML, SQL e o escambau, nós precisamos abrir
eles de formas diferentes com um trabalhão, com o uso do pandas, nos podemos fazer isso muuuito mais fácil e geralmente
em uma única linha como veremos a baixo'''

#Para estudarmos isso vamos ver algo que permite-nos abrir um mooonte de databases normalizados de invertimentos,
#que é chamado de Quandl, ele é bem interessante pelo o que parece

#No site você consegue uns códigos que pode ser referente diretamente a linguagem que você tá usando para carregar
#seus dados

#O pandas tem uma excelente documentação, para tentar abrir um tipo de arquivo especifico, basta pesquisar
#IO pandas, lá ele te mostra os métodos para ler e escrever, respectivamente

import pandas as pd
import matplotlib.pyplot as plt
#from matplotlib import Style
import numpy as np

#Peguei o código e o arquivo csv fazendo a conta no Quandl, o arquivo eu baixei de: goo.gl/NPoYEC
#Como o arquivo csv se encontra no mesmo folder, eu só preciso dizer o nome dele e usar o método que diz no doc.

df = pd.read_csv('ZILLOW-Z77006_ZRIMFRR.csv')

print(df.head())

df.to_csv('newcsv2.csv') #Basicamente nos só escrevemos o dataFrame como um arquivo csv

#Podemos abrir o arquivo csv e já especificar qual coluna será seu index atribuindo o index_col

#df = pd.read_csv('newcsv2.csv', index_col = 0) Samerd4 n funciona mais n

#Imagine que nos tenhamos várias colunas de valores para várias cidades, nós podemos renomear essas colunas diretamente:
df.columns = ['Data','Austin_HIP']
print(df.head())

#Ou podemos renomear apenas uma coluna, ou então algumas escolhidas apenas, com o método rename
df.rename(columns = {'Austin_HIP' : 'Precinhos_Austin'}, inplace = True)
print(df.head())

#Podemos salvar agora e o que for salvo estará com os nomes das colunas alterados
#Caso queiramos guardar apenas os dados e não informar os nomes dessas colunas, basta colocar Headers = False, o nome das colunas pelo pandas são chamadas de Headers

df.to_csv('newcsv3.csv', header = False)

#Ao abrir um arquivo que não contenha headers, podemos atribuir nomes as colunas no momento da leitura

df = pd.read_csv('newcsv3.csv', names=['Datinha', 'Austin_HIP'])

print(df.head())

#Uma coisa muito foda do pandas é que ele pode fazer transformações entre os formatos automaticamente
#de uma forma muuuuuuuito easy

df.to_html('demonstracao.htlm')








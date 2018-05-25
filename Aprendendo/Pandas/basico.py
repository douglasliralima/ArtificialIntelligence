import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style #Basicamente usaremos isso para definir o estilo da nossa plotagem
import numpy as np

style.use('ggplot')

#No pandas basicamente todos os arquivos que vamos carregar, sejam eles csv, html, ou o caralh0 a 4, nos vamos carregar
#na forma de dicionarios, esses dicionarios serão transformados em dataframes, que é uma variação dos dicionarios
#feito pelo pandas, que possui alguams funcoes muito úteis

horarios = {'Dia:' : [1,2,3,4,5,6],
			'Estudando' : [5,6,3,6,5,7],
			'Dormindo' : [4,6,7,5,5,6]}

df = pd.DataFrame(horarios) #Podemos transformar diretamente dicionarios em dataframes '-'

#print(df.head()) #Essa funcao basicamente imprime os primeiros 5 elementos do dataframe
#print(df.tail()) #Essa funcao basicamente imprime os últimos 5 elementos do dataframe

print(df) #Veja, agora eles são organizados em forma de tabela

#O pandas geralmente define um index padrao de 0 até o ultimo elemento em seu dataframe, mas podemos definir
#um elemento do nosso dicionario, como um index próprio do dataframe

df2 = df.set_index('Dia:')

print(df2)

#Veja, esse método retorna um dataframe modificado, não modifica o objeto estaticamente, o que você pode fazer
#para trabalhar encima disso é sobreescrever seu dataframe, como fizemos, ou usar um de um atributo pelo conceito
#de polimorfismo que é o atributo inplace = True, ele altera o objeto em si

df.set_index('Dia:', inplace = True)

#Podemos referenciar uma especifica coluna com o mesmo esquema que os dicionarios ou acessar como um atributo

#print(df['Dormindo'])

print(df.Dormindo)

#Para referenciar mais de uma coluna, precisamso de duas barras para fazer uma lista de colunas
print(df[['Dormindo', 'Estudando']])

#Podemos transformar essas colunas em listas

print(df.Dormindo.tolist())

#Para transformar duas colunas em dois arrays, tendo um array bidimensional, precisamos usar o numpy ao invés do
#pandas

print(np.array(df[['Dormindo', 'Estudando']]))

#Uma coisa interessante que podemos fazer também é ir transformando apenas com as listas diretamente

df2 = pd.DataFrame(np.array(df[['Dormindo', 'Estudando']]))
print(df2)
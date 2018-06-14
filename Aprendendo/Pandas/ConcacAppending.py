import pandas as pd

#Vamos usar esses dicionarios para criarmos os nossos dataFrames apenas para exemplificação

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

#Veja que o dataframe 1 e 2, possuem os mesmos index, mas colunas diferentes, já o 2º e o 3º possuem diferentes colunas e indices
#Para concatenar novas linhas em nosso dataframe é bem simples, basta elas compartilharem das mesmas colunas e terem indices diferentes
#Basta usarmos o método concat e passarmos como parâmetro uma lista de dataframes
concat = pd.concat([df1, df2])

##print(concat)

#Agora e se concatenassemos o df3 também?

concat = pd.concat([df1,df2,df3])

#print(concat)

#Veja, é adicionada uma nova coluna que nenhum dos outros dataframes tem, o df3 é colocado embaixo na tabela e
#a coluna que ele n tem, também é adicionada resultando em outros NaN, basicamente a concatenacao só adiciona embaixo

#O método append faz a mesma coisa que o método concat, sem tirar nem por pd.append(dataframes)
#Podemos criar uma linha separada e depois colocarmos em nosso DataFrame, mas o pandas não é exatamente o melhor do mundo em
#fazer entrada de dados gradual em nossos dataframe, ele é melhor apenas em manipula-los, mas podemos fazer alguams coisinhas anyway

s = pd.Series([80,2,50], index=['HPI','Int_rate','US_GDP_Thousands']) #Criamos uma linha, com esses nomes no dicionario
df4 = df1.append(s, ignore_index=True) #Como n add uma coluna de index, vamos ignorar todos eles para fazer nosso append
print(df4)
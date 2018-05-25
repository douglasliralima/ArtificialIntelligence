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

print(concat)
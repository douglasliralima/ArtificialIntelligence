import pandas as pd
#Vamos usar os mesmos dados do concating and appending

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

#-------------------Merging----------------------------
#Bom merging basicamente vai fazer um mix com seus dados sem ligar muito para os index
#Veja que fazendo isso, ele apenas junta as linhas daquilo que não é igual, mas não duplica aquilo que já existe nos dois
#Ainda deixa em ordem
print(pd.merge(df1, df2, on=['HPI', 'Int_rate']))

#------------------Joining----------------------------
#Ele se baseia justamente em nosso index, vamos demonstrar isso settando df1 e df3 por HPI como index e então, juntando eles
#como nesse caso, eles terão os mesmos int_rate, a única coisa que ele fará é adicionar uma nova coluna em nosso dataset

df1.set_index('HPI', inplace=True)
df3.set_index('HPI', inplace=True)

joined = df1.join(df3)#How vai falar se o objeto que chama ficará a frente ou atrás na joinação
print(joined)

#Esse tipo de coisa é bem melhor de se fazer com um banco de dados, se você tiver precisamos de mais informações a respeito
#Existem muitas particularidades, vá ver o site: goo.gl/4ytJhQ

import matplotlib.pyplot as plt #Esse é a classe com os métodos mais usadas nas aplicacoes com o matplotlib

x = [1,2,3]
y = [1,2,3]
#plt.plot(x,y) #Essa é uma funcao simples que coloca na tela um gráfico em R²
#Poderiamos mandar como parametro diretamente a lista, mas foda-se

'''
Tal qual o openGL, nos fazemos nossas paradas por trás e então colocamos isso em um ambiente
gráfico para poder desenhar na tela
'''
#plt.show()

#Veja, formamos um gráfico linear, podemos arrastar esse gráfico, redimencionar tela, dar zoom, salvar a imagem
'''
Geralmente é muito útil nos deixarmos o nosso gráfico com:
Título
legenda
nomeação de x e y...
'''
plt.title('Meu primeiro grafico :,)')

plt.plot(x,y, label = 'a = 1 & b = 0')
x2 = [1,2,3]
y2 = [2,4,6]
plt.plot(x2,y2, label = 'a = 2 & b = 0')
plt.legend()#Habilitamos que a legenda label, apareça

plt.xlabel('Variacao em x')#Nomeia o eixo x
plt.ylabel('Variacao em y')#Nomeia o eixo y

plt.show()
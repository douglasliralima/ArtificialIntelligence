import matplotlib.pyplot as plt

plt.title('Outras plotagens')
#-------------------------------------------BAR CHART-----------------------------------------
'''
plt.xlabel('x')
plt.ylabel('y')
x = [1,3,5]#Será considerado de o meio de onde sai a nossa barra
y = [20,40,60]#Sera a altura da barra


plt.bar(x,y,label = 'Só vai amarelao', color = 'yellow')

'''
'''Se nos colocassemos outra barra, sem o color, elas ficariam com a mesma cor, mesmo estando com legendas diferentes
para arrumar isso, nós então, podemos settar como um dos parâmetros a cor pelo nome padrão ou por seu
respectivo código hexadecimal
'''
'''
x2 = [2,4]
y2 = [30,50]

plt.bar(x2,y2,label = "So vai azulao", color = "blue")

plt.legend() #Habilita as legendas sempre depois de plotar
plt.show()
'''
#---------------------------------------------------Histograms-----------------------------------------
'''
Basicamente histograms são gráficos de barras melhorados, onde temos um range, em que as coisas são contidas
dando a base dos elementos que estão nessa merd4 toda contida
Vou fazer igual ao exemplo passado e criar uma cidade ficticia, em que eu vou encher ela com idades
e definir um range de até onde as coisas podem variar 
'''
idade_populacao = [5,2,3,12,41,23,21,26,75,12,34,52,12,67,96,12,7,5,67,65,31,31,31,35,32,37,30,35,42,25,26,24,21,29,28]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]#Traducao de bins = caixas
'''Esses bins basicamete serão uma caixa que vão conter os elementos entre a primeira casa e a segunda, sucetivamente
até 100, nesse caso seria 0~10, 10~20, 20~30...
'''

plt.hist(idade_populacao, bins, histtype = 'bar', rwidth = 0.8)
#Existem outros tipos de histograms que você pode pesquisar depois e definir eles no histtype
#Rwith é o quanto do range as barras vão poder consumir em seu tamanho compartilhado

plt.show()
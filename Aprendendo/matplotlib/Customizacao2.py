import matplotlib.pyplot as plt

escolha = int(input("Você deseja\n" +"1- Ver as legendas dos eixos pintadas e altadas\n" +
					"2-Preenchimento de gráfico\n"))

if(escolha == 1):
	#Em uma plotagem qualquer, podemos definir uma cor para as legendas dos eixos x e y
	graf1 = plt.subplot2grid((1,1),(0,0))
	graf1.plot(range(10))
	plt.xlabel('x')
	plt.ylabel('y')
	graf1.xaxis.label.set_color('b')
	graf1.yaxis.label.set_color('r')
	#Outra coisa interessante é que podemos alterar os valores de metragem mostradas ao usuário de acordo com aquilo que a gente quer
	graf1.set_yticks([0,3,6,9,12]) #Settando apenas para o y, por isso yticks
	#Também é legal settar cor para os nossos instantes e não deixar full preto, nunca é legal, fica pouco friendly
	graf1.tick_params(axis = 'x', colors = "red")
	plt.show()

else:
	graf1 = plt.subplot2grid((1,1),(0,0))
	#Vamos preencher a linha formada em y por [1,2,3] e x por [1,2,3] e o eixo 0
	#graf1.fill_between([1,2,3], [1,2,3], 0, alpha=0.3)
	#Mas não só em relação ao plano y=0, podemos preencher em relação a outros planos em y
	#Uma coisa que pode acontecer é quando você preenche um gráfico, você acabar sobrepondo outra coisa, para resolver isso
	#usamos essa coordenada alpha(transparência)

	graf1.fill_between([1,2,3], [4,2,4], 3, facecolor = 'g', alpha=0.3)#Aumentei o y inicial para demonstrar o que acontece quando se está abaixo
	#Podemos colocar no lugar desse 3 alguma operação lógica, o que é bem interessante para fazer visualização
	#Com essa operação lógica fica melhor para fazer lucros e perdas
	#Não tem como eu demonstrar aqui sem uma API de lucros ou coisas assim sem fazer alguma computação complicada

	#Outra coisa legal que podemos fazer é alterar a cor da moldura da janela que está o nosso plot ou então retirar uma das molduras
	graf1.spines['left'].set_color('green')
	graf1.spines['left'].set_linewidth(3)
	graf1.spines['right'].set_visible(False)
	graf1.spines['top'].set_visible(False)

	plt.show()

#Vamos ver como fazer certos preenchimentos em nosso gráfico


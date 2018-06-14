import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,4,6,8,10]

'''plt.plot(x,y, label="y=2x")
plt.xlabel("Valores em x")
plt.ylabel("Valores em y")
plt.title("CustomizacaoBasica")
#Nos podemos guardar a figura resultante dessas nossas manipulações em uma variável
#graf1 = plt.figure()
'''
tipo_rotacao = int(input("Tipo de rotacao 1 ou 2?\n"))
if(tipo_rotacao == 1):
	#Podemos fazer subplotagens em nosso plot
	plt.subplot(311)
	plt.plot([1,2,3], [2,4,6], 'o')

	plt.subplot(312)
	plt.plot(range(12))

	plt.subplot(313)
	plt.plot([1,2,3], [2,4,6], 'D')

	#Nos podemos rotacionar as valorações do gráfici em x ou y através do comando abaixo, passando quantos graus ele precisa girar
	plt.xticks(rotation=45)
	#Nos podemos configurar os espaçamentos dos subplots indo em configure subplots ao lado da lupazinha e configura-los manualmente
	#plt.subplots_adjust(bottom=0.10) #Ou fazer pelo código, coloque outros atributos a medida do que você quer
	plt.grid(True)
	plt.show()

#Segunda forma de plotação e rotação dos eixos
else:
	print("Man at work")
	#Nos podemos guardar uma figura resultante de uma plotagem em uma variável
	plt.plot([1,2,3], [2,4,6], 'o')
	plt.grid(True)#Para deixar uma matriz na plotagem 1

	fig = plt.figure() #Podemos guardar a figura da nossa plotagem
	#Para criarmos uma segunda plotagem em outra janela precisamos cria-la fora do default
	#Com esse fim, falamos a proporção do nosso plano e onde é sua origem e grardamos isso em uma variável subplot
	graf1 = plt.subplot2grid((1,1), (0,0)) #Altere a primeira tupla para 5,5 e veja a diferença de proporção
	#Ao fazermos as modificações nessa variável
	graf1.plot(range(12))
	#Ela fica guardada e é plotada junto com a default

	#Podemos modificar individualmente cada um dos números em algum dos eixos, vamos fazer no x e rotacionar todos em 45º
	for label in graf1.xaxis.get_ticklabels(): #Vou pegar cada uma das coordenadas e salvar em label
		label.set_rotation(45) #Girando ela em 45º

	plt.xlabel('x')
	plt.ylabel('y')
	plt.grid(True, color = 'g', linestyle = '-', linewidth = 2)#Veja, podemos personalizar o grid, settando sua cor, o formato da linha, a grossura dela
	plt.show()

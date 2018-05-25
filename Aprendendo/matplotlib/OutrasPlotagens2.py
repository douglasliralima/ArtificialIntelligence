import matplotlib.pyplot as plt

#-----------------------Scatterplots----------------------
'''
São muito úteis para verificar correlação de dados, e assim poder eliminar um deles
'''
'''
x = [1,5,2,4,12,7,2,6]
y = [1,2,5,7,4,7,1,2]

plt.scatter(x, y, label = 'dadosLoucos', color = 'red', s = 50, marker = "*")
'''
'''
s(size) vai ser o tamanhozinho que o pontinho vai ser representado no gráfico
marker vai ser o tipo do ponto que vamos representar nossos elementos
assim como as cores, há uma pohh4da de marker que vc pode ver no proprio site do matplotlib
'''
'''
plt.xlabel('x')
plt.ylabel('y')
plt.title('Grafico do PT')
plt.legend()
plt.show()
'''
#--------------------StackPlot---------------------------------
#Ele é um bom jeito de visualizar a a largura de seus dados em relação aos outros
'''
dias = [1,2,3,4,5]

dormindo = [3,5,4,5,6]
estudando = [6,8,7,8,4]
trabalhando = [4,2,5,6,7]

plt.stackplot(dias, dormindo,estudando,trabalhando, colors = ['m', 'c', 'r']) #Fica cagado sem legenda
#Nos nao podemos add legendas normalmente, por preguiça de implementacao do matplotlib, entao fazemos linhas fakes e implementamos as legendas
plt.plot([], [], color = 'm', label = 'dormindo', linewidth = 5)
plt.plot([], [], color = 'c', label = 'estudando', linewidth = 5)
plt.plot([], [], color = 'r', label = 'trabalhando', linewidth = 5)
#Veja que basicamente nao plotamos nada na tela, mas usamos apena a legenda disso
#linewidth Com isso nós podemos configurar a largura da linha
plt.legend()
plt.show()'''
#--------------------------PieChart----------------------------
#Esse é basicao do ensino medio

horas_obrigacoes = [8,4,4,8]
nomes = ['dormindo', 'estudando', 'trabalhando', 'PensandoNaMorena']
cores = ['w','c','m','r']

plt.pie(horas_obrigacoes,
 		labels = nomes,			#Vamos falar o nome de cada slice
 		colors = cores,			#Vamos dizer as cores de cada slice
 		startangle = 90,		#Define de onde comeca a plotacao, vai no sentido horario
 		shadow = True,			#Vai deixar um fundinho de sombra
 		explode = (0,0,0,0.1),	#Vai destacar algum dos slices
 		autopct = '%1.1f%%') 	#Vai fazer a porcentagem dos slices


#Ele segue plotando no sentido horario
plt.title("Horas do meu dia")
plt.legend()
plt.show()




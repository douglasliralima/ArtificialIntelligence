import matplotlib.pyplot as plt
import numpy as np

'''
Uma coisa muito comum é querermos abrir documentos de dados em csv ou outros arquivos
para usarmos o matplotlib, o segredo do sucesso aqui é muito simples, nos precisaremos entratanto
usar o numpy para nos auxiliarmos nessa empreitada e deixar as coisas muuuuuuuuuuuuuuuuuuuuuuito mais fácil
'''

x, y = np.loadtxt("exemplo.txt", delimiter = ",", unpack = True)
#Precisamos mostrar o caminho arquivo padrao
#O delimitador serve para dizer o que divide aquilo que vai para uma variavel e o que vai para outra, respectivamente
#O default do delimitador é um espaco em branco
#unpack, permite separar os arrays de retorno para cada elemento, ou seja é ele que deixa de uma vez a gente settar x e y
#Por default unpack é false

plt.plot(x,y, label = "y=x²")
plt.xlabel("Valores da 1º coluna")
plt.ylabel("Valores da 2º coluna")
plt.legend()
plt.title("Carregado do arquivo\nParabola Simples")
plt.show()
from socket import *

meuHost = "localhost"
portNumber = 50007

mensagem = "Manticore"

sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((meuHost, portNumber))

sockobj.send(mensagem.encode())

#dados = sockobj.recv(100000)
#print(dados)
import pandas as pd
import numpy as np
import math
import random

from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPRegressor
from sklearn import svm
from sklearn.decomposition import PCA
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.tree import DecisionTreeClassifier
#from sklearn.multioutput import RegressorChain
from sklearn.multioutput import MultiOutputRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.tree import ExtraTreeRegressor
from sklearn.svm import LinearSVR
from sklearn.svm import LinearSVC
from sklearn.linear_model import RidgeCV
from sklearn.ensemble import RandomForestRegressor
from collections import OrderedDict
from sklearn.multioutput import MultiOutputClassifier
from Process import Process


class Projeto:
        monsterIn = []
        monsterOut = [] 

        def __init__(self):
                #Primeira coisa que fazemos é carregar o nosso dataset em um objeto da classe DataFrame
                #Ele basicamente carrega o arquivo e coloca numa variável
                dados = pd.read_csv('Monstros.csv')


                dados = Process.preprocessMonster(dados)


                x_train = dados.drop(['Hit dice', 'Armor Class', 'Fortitude', 'Reflexes', 'Will', 'Str', 'Con', 'Int', 'Wis', 'Cha'], axis = 1)
                self.y_train = dados.drop(['Type', 'Syze', 'Enviroments', 'Alignment', 'LvL Adjustment', 'Challenge Rating'], axis = 1)

                '''
                tree1 = DecisionTreeClassifier(random_state = 4)
                tree1.fit(x_train, y_train)
                accuracyTree = tree1.score(x_test, y_test)

                print('Acuracia da Arvore de classificação:',accuracyTree)
                '''


                self.tree = DecisionTreeRegressor(random_state = 4)
                self.tree.fit(x_train, self.y_train)
                #accuracyTree = tree.score(x_test, y_test)

                #print('Acuracia da Arvore de decisão:',accuracyTree)


                self.regr_4 = RandomForestRegressor()
                self.regr_4.fit(x_train, self.y_train)
                #acuracia1 = regr_4.score(x_test, y_test)
                #print("Acuracia da RandomForestRegressor:", acuracia1)

                self.regr_5 = ExtraTreesRegressor()
                self.regr_5.fit(x_train, self.y_train)
                #acuracia2 = regr_5.score(x_test, y_test)
                #print("Acuracia das Arvores de regreção:", acuracia2)

                self.regr_3 = ExtraTreeRegressor()
                self.regr_3.fit(x_train, self.y_train)
                #acuracia2 = regr_3.score(x_test, y_test)
                #print("Acuracia da Arvore de regreção:", acuracia2)
                print("Inteligencia artificial inicializa")

        def setMonsterIn(self, type, size, environment, alignment, lvlAdjustment, challengeRating):
                self.monsterIn = OrderedDict([
                                ('Type', type),
                                ('Syze', size),
                                ('Enviroments', environment),
                                ('Alignment', alignment),
                                ('LvL Adjustment', lvlAdjustment),
                                ('Challenge Rating', challengeRating)
                                ])

        def getMonsterOut(self):
                #print(self.monsterIn)

                aux = pd.DataFrame(self.monsterIn, columns=self.monsterIn.keys(), index = [0])
                new_data_naonumeros = aux[['Type', 'Syze', 'Enviroments', 'Alignment']]
                print(new_data_naonumeros.head())
                new_data_numeros = aux.drop(['Type', 'Syze', 'Enviroments', 'Alignment'], axis = 1 )

                new_data_naonumeros = Process.traduzUsuario(new_data_naonumeros)
                #print(new_data_naonumeros, new_data_numeros, sep = '\n')

                aux = pd.concat([new_data_numeros, new_data_naonumeros], axis=1)
                #print(aux)

                monstro = {}
                for atributo in aux:
                	for elemento in aux[atributo]:
                		monstro[atributo] = elemento

                monstro_usuario = OrderedDict(sorted(monstro.items(), key=lambda t: len(t[0])))

                monstro = pd.Series(monstro_usuario).values.reshape(1,-1)

                predict1 = self.tree.predict(monstro)
                predict2 = self.regr_4.predict(monstro)
                predict3 = self.regr_3.predict(monstro)
                predict4 = self.regr_5.predict(monstro)

                numeros = predict1[0 , :]
                resultado1 = [int(x) for x in numeros]

                numeros = predict2[0 , :]
                resultado2 = [int(x) for x in numeros]

                numeros = predict3[0 , :]
                resultado3 = [int(x) for x in numeros]

                numeros = predict4[0, :]
                resultado4 = [int(x) for x in numeros]

                #print(self.monsterIn)
                #print("\n" * 2, "Resultado 1:", resultado1, sep = "\n")
                #print(Process.protocoloSaida(y_train, resultado1))
                #print("\n" * 2, "Resultado 2:", resultado2, sep = "\n")
                #print(Process.protocoloSaida(y_train, resultado2))
                #print("\n" * 2, "Resultado 3:", resultado3, sep = "\n")
                #print(Process.protocoloSaida(y_train, resultado3))
                #print("\n" * 2, "Resultado 4:", resultado4, sep = "\n")
                #print(Process.protocoloSaida(y_train, resultado4))

                artificialMonster = Process.protocoloSaida(self.y_train, resultado1)

                #=#=============================#=#========================================================================#=#
                #=# GERAÇÂO DOS ATRIBUTOS SEM IA #=#========================================================================#=#
                #=#=============================#=#========================================================================#=#
                '''
                ' Parte construida por Drayton Corrêa Filho (Drayton80)
                '''
                # LIFE BONUS and BASE AINITIATIVE #--------------------------------------------------------#
                lifeBonus = int((artificialMonster['Con']-10)/2)*artificialMonster['Hit dice']

                #initiative = int((artificialMonster['Dex']-10)/2)
                #---------------------------------#--------------------------------------------------------#

                # DICE TYPE and BASE ATTACK #--------------------------------------------------------------#
                # Aqui é observado o Tipo da criatura para poder checar seu tipo de dado e BBA à partir
                # da tabela 4-1: Creature Improvement by Type do Monster Manual 
                if(self.monsterIn['Type'] == "Aberration" or self.monsterIn['Type'] == "Animal" or
                   self.monsterIn['Type'] == "Elemental" or self.monsterIn['Type'] == "Giant" or
                   self.monsterIn['Type'] == "Humanoid" or self.monsterIn['Type'] == "Plant" or
                   self.monsterIn['Type'] == "Vermin"):
                        diceType = "d8"
                        dice = 8
                        baseAttack = int(artificialMonster['Hit dice']*3/4)

                elif(self.monsterIn['Type'] == "Construct" or self.monsterIn['Type'] == "Ooze"):
                        diceType = "d10"
                        dice = 10
                        baseAttack = int(artificialMonster['Hit dice']*3/4)

                elif(self.monsterIn['Type'] == "Dragon"):
                        diceType = "d12"
                        dice = 12
                        baseAttack = artificialMonster['Hit dice']

                elif(self.monsterIn['Type'] == "Fey"):
                        diceType = "d6"
                        dice = 6
                        baseAttack = int(artificialMonster['Hit dice']*1/2)

                elif(self.monsterIn['Type'] == "Magical Beast"):
                        diceType = "d10"
                        dice = 10
                        baseAttack = artificialMonster['Hit dice']

                elif(self.monsterIn['Type'] == "Monstrous Humanoid" or self.monsterIn['Type'] == "Outsider"):
                        diceType = "d8"
                        dice = 8
                        baseAttack = artificialMonster['Hit dice']

                elif(self.monsterIn['Type'] == "Undead"):
                        diceType = "d12"
                        dice = 12
                        baseAttack = int(artificialMonster['Hit dice']*1/2)
                #---------------------------#--------------------------------------------------------------#

                # GRAPPLE #--------------------------------------------------------------------------------#
                if(self.monsterIn['Syze'] == "Colossal"):
                        specialSizeModifier = 16

                elif(self.monsterIn['Syze'] == "Gargantuan"):
                        specialSizeModifier = 12

                elif(self.monsterIn['Syze'] == "Huge"):
                        specialSizeModifier = 8

                elif(self.monsterIn['Syze'] == "Large"):
                        specialSizeModifier = 4

                elif(self.monsterIn['Syze'] == "Medium"):
                        specialSizeModifier = 0

                elif(self.monsterIn['Syze'] == "Small"):
                        specialSizeModifier = -4

                elif(self.monsterIn['Syze'] == "Tiny"):
                        specialSizeModifier = -8

                elif(self.monsterIn['Syze'] == "Diminutive"):
                        specialSizeModifier = -12

                elif(self.monsterIn['Syze'] == "Fine"):
                        specialSizeModifier = -16


                grapple = baseAttack + int((artificialMonster['Str']-10)/2) + specialSizeModifier
                #---------#--------------------------------------------------------------------------------#

                # HIT POINTS #-----------------------------------------------------------------------------#
                hitPoints = 0

                i = 1

                # Faz um while que cálcula cada rolagem de dados para vida:
                while (i <= artificialMonster['Hit dice']):
                    # Simula à rolagem de um dado fazendo um random integer que vai
                    # de 1 até o número máximo do dado especificado pela variável dice
                    hitPoints += random.randint(1, dice)

                    i += 1

                hitPoints += lifeBonus
                #------------#-----------------------------------------------------------------------------#

                #=#==============================#=#========================================================================#=#
                #=#=============================#=#========================================================================#=#

                #print("Life Bônus: ", lifeBonus)
                #print("Initiative: ", initiative)
                #print("Dice Type: ", diceType)
                #print("Base Attack: ", baseAttack)
                #print("Grapple: ", grapple)


                monsterToClient = (self.monsterIn['Type'] + "," + self.monsterIn['Syze'] + "," + str(hitPoints) + "," +
                str(baseAttack) + "," + str(grapple) + "," +
                str(artificialMonster['Fortitude']) + "," + str(artificialMonster['Reflexes']) + "," + 
                str(artificialMonster['Will']) + "," + str(artificialMonster['Str']) + "," + 
                str(artificialMonster['Con']) + "," +
                str(artificialMonster['Int']) + "," + str(artificialMonster['Wis']) + "," +
                str(artificialMonster['Cha']) + "," + str(self.monsterIn['Enviroments']) + "," + 
                str(self.monsterIn['Challenge Rating']) + "," + self.monsterIn['Alignment'])

                #print(monsterToClient)

                '''
                monsterToClient = (self.self.monsterIn['Type'] + "," + self.self.monsterIn['Syze'] + "," + str(artificialMonster['Hit dice']) + "," +
                str(diceType) + "," + str(lifeBonus) + "," + str(initiative) + "," + str(baseAttack) + "," + str(grapple) + "," +
                str(artificialMonster['Fortitude']) + "," + str(artificialMonster['Reflexes']) + "," + 
                str(artificialMonster['Will']) + "," + str(artificialMonster['Str']) + "," + 
                str(artificialMonster['Dex']) + "," + str(artificialMonster['Con']) + "," +
                str(artificialMonster['Int']) + "," + str(artificialMonster['Wis']) + "," +
                str(artificialMonster['Cha']) + "," + str(self.self.monsterIn['Enviroments']) + "," + 
                str(self.self.monsterIn['Challenge Rating']) + "," + self.self.monsterIn['Alignment'])
                '''
                
                return monsterToClient


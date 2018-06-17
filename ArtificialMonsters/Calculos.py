artificialMonster = Process.protocoloSaida(y_train, resultado1)

# LIFE BONUS and BASE AINITIATIVE #--------------------------------------------------------#
lifeBonus = artificialMonster['Con']*artificialMonster['Hit dice']

initiative = artificialMonster['Des']
#---------------------------------#--------------------------------------------------------#

# DICE TYPE and BASE ATTACK #--------------------------------------------------------------#
# Aqui é observado o Tipo da criatura para poder checar seu tipo de dado e BBA à partir
# da tabela 4-1: Creature Improvement by Type do Monster Manual 
if(new_data['Type'] == "Aberration" || new_data['Type'] == "Animal" ||
   new_data['Type'] == "Elemental" || new_data['Type'] == "Giant" ||
   new_data['Type'] == "Humanoid" || new_data['Type'] == "Plant" ||
   new_data['Type'] == "Vermin"):
	diceType = "d8"
	baseAttack = int(artificialMonster['Hit dice']*3/4)

elif(new_data['Type'] == "Construct" || new_data['Type'] == "Ooze"):
	diceType = "d10"
	baseAttack = int(artificialMonster['Hit dice']*3/4)

elif(new_data['Type'] == "Dragon"):
	diceType = "d12"
	baseAttack = artificialMonster['Hit dice']

elif(new_data['Type'] == "Fey"):
	diceType = "d6"
	baseAttack = int(artificialMonster['Hit dice']*1/2)

elif(new_data['Type'] == "Magical Beast"):
	diceType = "d10"
	baseAttack = artificialMonster['Hit dice']

elif(new_data['Type'] == "Monstrous Humanoid" || new_data['Type'] == "Outsider"):
	diceType = "d8"
	baseAttack = artificialMonster['Hit dice']

elif(new_data['Type'] == "Undead"):
	diceType = "d12"
	baseAttack = int(artificialMonster['Hit dice']*1/2)
#---------------------------#--------------------------------------------------------------#

# GRAPPLE #--------------------------------------------------------------------------------#
if(new_data['Syze'] == "Colossal"):
	specialSizeModifier = 16

elif(new_data['Syze'] == "Gargantuan"):
	specialSizeModifier = 12

elif(new_data['Syze'] == "Huge"):
	specialSizeModifier = 8

elif(new_data['Syze'] == "Large"):
	specialSizeModifier = 4

elif(new_data['Syze'] == "Medium"):
	specialSizeModifier = 0

elif(new_data['Syze'] == "Small"):
	specialSizeModifier = -4

elif(new_data['Syze'] == "Tiny"):
	specialSizeModifier = -8

elif(new_data['Syze'] == "Diminutive"):
	specialSizeModifier = -12

elif(new_data['Syze'] == "Fine"):
	specialSizeModifier = -16


grapple = baseAttack + specialSizeModifier
'''TO DO Modificador +''' 
#---------#--------------------------------------------------------------------------------#





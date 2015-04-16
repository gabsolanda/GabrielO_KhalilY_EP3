# -*- coding: utf-8 -*-
"""
Exercício Projeto 3:
Dupla:
      Gabriel Olanda
      Khalil Yassine 
      
"""
###############################################################################
"""
Definindo as funções de TMB
"""
#Fórmula de Harris-Benedict para MULHERES.
def TMBwoman (idade, peso, altura):
    return 447.6+(9.2*peso)+(3.1*altura)-(4.3*idade)
        
#Fórmula de Harris-Benedict para HOMENS.
def TMBman (idade, peso, altura):
    return 88.36+(13.4*peso)+(3.1*altura)-(5.7*idade)

        
###############################################################################
       
        
"""
Abrindo o arquivo alimentos.csv e lendo as linhas do arquivo, além de criar 
dicionários para os dados em seu interior
"""

arquivo= open("alimentos.csv", encoding="latin1")
lista = arquivo.readlines() 

CAL_dic = {}
tab = {}

for l in lista[1:]:
    pedacos = l.strip().split(",")
    #print(pedacos[:3])
    
    # Dicionario que vai ser a tabela de calorias para cada alimento. Cal/100g
    tab[pedacos[0]] = float(pedacos[2])/float(pedacos[1])
    #print (tab)
    
###############################################################################
"""
Recolhendo os dados das GORDURAS do arquivo alimentos.csv e salvando em um di
cionário chamado gordura.
"""

gordura = {}

for g in lista[1:]:
    gord = g.strip().split(',')
    gordura[gord[0]] = float(gord[5])/float(gord[1])
    #print (gordura)

###############################################################################
"""
Recolhendo os dados das PROTEINAS do arquivo alimentos.csv e salvando em um di
cionário chamado proteina.
"""

proteina = {}

for p in lista[1:]:
    prote = p.strip().split(',')
    proteina[prote[0]] = float(prote[3])/float(prote[1])
###############################################################################   
"""
Recolhendo os dados das CARBOIDRATOS do arquivo alimentos.csv e salvando em um 
dicionário chamado carboidratos.
"""

carboidratos = {}

for c in lista[1:]:
    carbo = c.strip().split(',')
    carboidratos[carbo[0]] = float(carbo[4])/float(carbo[1])

###############################################################################   
"""   
Abre o arquivo com os dados do usuário.  
""" 
arquivou = open('usuario.csv', encoding = 'latin1')
listau = arquivou.readlines()

tabu = {}

# Incorpora os dados do usuário, como idade nome e etc.
for n in listau[1:2]:
    pedacosu = n.strip().split(';')
    print (pedacosu)
    nome = pedacosu[0]
    idade = int(pedacosu[1])
    peso = float(pedacosu[2])
    sexo = pedacosu[3]
    altura = float(pedacosu[4])
    fator = pedacosu[5]
    
for c in listau[3:]:
    comeu = c.strip().split(';')
    
    if comeu[0] in tabu:
        tabu[comeu[0]] += tab[comeu[1]]*float(comeu[2])
    else:
        tabu[comeu[0]] = tab[comeu[1]]*float(comeu[2])
        
print(tabu)

###############################################################################
"""
Fórmula de Harris-Benedict para homens.
"""
F = 0
M = 0

if sexo == 'F':
    f = TMBwoman(idade, peso, altura)

###############################################################################    
"""
Fórmula de Harris-Benedict para mulheres.

"""
if sexo == 'M':   
   m = TMBman(idade, peso, altura)
   print (m)
   

    
    






        
        
        
# -*- coding: utf-8 -*-
"""
Exercício Projeto 3:
Dupla:
      Gabriel Olanda
      Khalil Yassine 
      
"""
###############################################################################
"""
Fazendo os imports
"""
import doctest
import matplotlib.pyplot as plt

###############################################################################
"""
Definindo as funções de TMB
"""
#Fórmula de Harris-Benedict para MULHERES.
def TMBwoman (idade, peso, altura):
    """
    Calcula TMB para mulheres
    >>> TMBwoman (30, 70, 1.64)
    967.684
    """
    return 447.6+(9.2*peso)+(3.1*altura)-(4.3*idade)
    
if __name__=="__main__":
    doctest.testmod(verbose="True")
        
#Fórmula de Harris-Benedict para HOMENS.
def TMBman (idade, peso, altura):
    """
    Calcula o TMB para homens
    >>> TMBman(30, 70, 1.64)
    860.444
    """
    return 88.36+(13.4*peso)+(3.1*altura)-(5.7*idade)
    
if __name__=="__main__":
    doctest.testmod(verbose="True")

        
###############################################################################
       
        
"""
Abrindo o arquivo alimentos.csv e lendo as linhas do arquivo, além de criar 
dicionários para os dados em seu interior
"""

arquivo= open("alimentos.csv", encoding="latin1")
lista = arquivo.readlines() 

CAL_dic = {}
tab = {}
tabg = {}
tabp = {}
tabc = {}

for l in lista[1:]:
    pedacos = l.strip().split(",")
    #print(pedacos[:3])
    
    # Dicionario que vai ser a tabela de calorias para cada alimento. Cal/100g
    tab[pedacos[0]] = float(pedacos[2])/float(pedacos[1])
    # Dicionario que vai ser a tabela de gorduras para cada alimento. G/100g
    tabg[pedacos[0]] = float(pedacos[5])/float(pedacos[1])
    # Dicionario que vai ser a tabela de PROTEINAS para cada alimento. P/100g
    tabp[pedacos[0]] = float(pedacos[3])/float(pedacos[1])
    # Dicionario que vai ser a tabela de CARBOIDRATOS para cada alimento. C/100g
    tabc[pedacos[0]] = float(pedacos[4])/float(pedacos[1])
    
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
    #print (proteina)
###############################################################################   
"""
Recolhendo os dados das CARBOIDRATOS do arquivo alimentos.csv e salvando em um 
dicionário chamado carboidratos.
"""

carboidratos = {}

for c in lista[1:]:
    carbo = c.strip().split(',')
    carboidratos[carbo[0]] = float(carbo[4])/float(carbo[1])
    #print (carboidratos)
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
    
    
""" 
Tabela com calorias consumidas por dia
"""
    
for c in listau[3:]:
    comeu = c.strip().split(';')
    #print (comeu)
    if comeu[0] in tabu:
        tabu[comeu[0]] += tab[comeu[1]]*float(comeu[2])
    else:
        tabu[comeu[0]] = tab[comeu[1]]*float(comeu[2])
        
#print(tabu)
###############################################################################
"""
Tabela com gorduras consumidas por dia
"""
tabug = {}

for go in listau[3:]:
    gordo = go.strip().split(';')
    #print (gordo)
    if gordo[0] in tabug:
        tabug[gordo[0]] += tabg[gordo[1]]*float(gordo[2])
    else:
        tabug[gordo[0]] = tabg[gordo[1]]*float(gordo[2])
#print(tabug)
    
###############################################################################
"""
Tabela com carboidratos consumidos por dia
"""
tabuc = {}

for ca in listau[3:]:
    carboi = ca.strip().split(';')
    #print (carboi)
    if carboi[0] in tabuc:
        tabuc[carboi[0]] += tabc[carboi[1]]*float(carboi[2])
    else:
        tabuc[carboi[0]] = tabc[carboi[1]]*float(carboi[2])
#print(tabuc)
###############################################################################
"""
Tabela com proteinas consumidas por dia
"""
tabup = {}

for po in listau[3:]:
    pro = po.strip().split(';')
    #print (pro)
    if pro[0] in tabup:
        tabup[pro[0]] += tabp[pro[1]]*float(pro[2])
    else:
        tabup[pro[0]] = tabp[pro[1]]*float(pro[2])
#print(tabup)
###############################################################################
"""
Fazendo uma lista para o gráfico com as CALORIAS consumidas
"""
CAL = []
for cal in tabu.values():
    CAL.append(cal)
#print (CAL)

###############################################################################
"""
Fazendo uma lista para o gráfico com as GORDURAS consumidas
"""
GORD = []
for gor in tabug.values():
    GORD.append(gor)
#print (GORD)

###############################################################################
"""
Fazendo uma lista para o gráfico com os CARBOIDRATOS consumidos
"""
CAR = []
for car in tabuc.values():
    CAR.append(car)
#print (CAR)

###############################################################################
"""
Fazendo uma lista para o gráfico com as PROTEÍNAS consumidas
"""
PRO = []
for pro in tabup.values():
    PRO.append(pro)
#print (PRO)

##---##---##---##---##---##---##---##---##---##---##---##---##---##---##---##--
"""
Fazendo uma lista com as datas para fazer o dicionário
"""
DATAS = []
for dt in tabug.keys():
    DATAS.append(dt)
    
#print (DATAS)
###############################################################################
"""
Fórmula de Harris-Benedict para homens.
"""
F = 0
M = 0

if sexo == 'F':
    f = TMBwoman(idade, peso, altura)
    if fator == 'minimo':
        at = f * 1.2
        print(at)
       
    elif fator == 'baixo':
        at = f * 1.375
        print(at)
       
    elif fator =='medio':
        at = f * 1.55
        print(at)
       
    elif fator == 'alto':
        at = f * 1.725
        print(at)
       
    elif fator == 'muito ativo':
        at = f * 1.9
        print(at)

###############################################################################    
"""
Fórmula de Harris-Benedict para mulheres.

"""
if sexo == 'M':   
    m = TMBman(idade, peso, altura)
    #print (m)
    if fator == 'minimo':
        at = m * 1.2
        print(at)
       
    elif fator == 'baixo':
        at = m * 1.375
        print(at)
       
    elif fator =='medio':
        at = m * 1.55
        print(at)
       
    elif fator == 'alto':
        at = m * 1.725
        print(at)
       
    elif fator == 'muito ativo':
        at = m * 1.9
        print(at)
    
###############################################################################
   
"""
Calculando o IMC do usuário e determinando se o usuário esta gordo ou não.
"""

def IMC (peso, altura):
    """
    Calculando o IMC do usuário
    >>> IMC (70, 1.64)
    33.834027364663896
    """
    return 1.3 * (peso/altura**2)
    
if __name__=="__main__":
    doctest.testmod(verbose="True")
    
imc = IMC (peso, altura)

for c in tabu.values():
    delta = at - c
#print (delta)

if 18.5 <= imc and imc <= 24.9:
    texto = open("arquivo.txt", "w")
    texto.writelines(str(imc)+'. Parabéns, você está com um IMC apropriado para sua estatura. Você comeu' + "str(delta)" + "kcal")
    texto.close()

elif imc < 18.5:
    texto = open("arquivo.txt", "w")
    texto.writelines(str(imc)+'. Procure um especialista, você está abaixo do peso')
    texto.close()
    
    
elif 25 <= imc and imc <= 29.9:
    texto = open("arquivo.txt", "w")
    texto.writelines(str(imc)+'. Procure um especialista, você etá acima do peso (Sobrepeso)')
    texto.close()
    
    
elif imc >= 30:
    texto = open("arquivo.txt", "w")
    texto.writelines(str(imc)+'. Cuidado, procure um especialista pois você está obeso(a).Você comeu ' + str(delta) + " kcal")
    texto.close()
                
###############################################################################
"""
Arrumando as listas das datas para fazer os gráficos
"""

dias = []
for i in range(0, len(DATAS)):
    w = str(DATAS[i])
    w = w.split('/')
    dias.append(float(w[0]))
#print (dias)
    
#recomendado
listar=[at]*len(dias)    
###############################################################################
"""
Fazendo gráficos
"""
plt.plot(dias, CAL, label = 'Consumidas')
plt.axis([6, max(dias), 0, 3000])
plt.plot(dias, listar, label = 'Recomendado')
plt.ylabel('Calorias [kcal]')
plt.xlabel('Dias')
plt.title(r'Quantidade de Calorias')
plt.legend()
plt.show()

plt.plot(dias, GORD, label = 'Gorduras')
plt.plot(dias, CAR, label = 'Carboidratos')
plt.plot(dias, PRO, label = 'Proteínas')
plt.axis([6, max(dias), 0, 200])
plt.ylabel('Gorduras (g);\n Carboidratos (g);\n Proteínas (g);')
plt.xlabel('Dias')
plt.title(r'Quantidade de Carboidratos, Proteínas e Gorduras')
plt.legend()
plt.show()



        
        
        

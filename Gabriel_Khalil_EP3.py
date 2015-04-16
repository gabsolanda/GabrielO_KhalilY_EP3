# -*- coding: utf-8 -*-
"""
Exercício Projeto 3:
Dupla:
      Gabriel Olanda
      Khalil Yassin
      
"""
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
    print(pedacos[:3])
    
    # Dicionario que vai ser tabela de calorias para cada alimento. Cal/100g
    tab[pedacos[0]] = float(pedacos[2])/float(pedacos[1])
    #print (tab)
    
    
arquivo1 = open('usuario.csv', encoding = 'latin1')
lista1 = arquivo1.readlines()




    
    






        
        
        
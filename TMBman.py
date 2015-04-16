# -*- coding: utf-8 -*-
"""
Fórmula de Harris-Benedict para homens.

"""

def TMBman (idade, peso, altura):
    return 88.36 + (13.4*peso) + (3.1*altura) - (5.7*idade)
    

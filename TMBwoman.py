# -*- coding: utf-8 -*-
"""
Fórmula de Harris-Benedict para mulheres.

"""

def TMBwoman (idade, peso, altura):
    return 447.6+(9.2*peso)+(3.1*altura)-(4.3*idade)


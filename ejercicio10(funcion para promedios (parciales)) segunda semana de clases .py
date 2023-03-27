# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:44:25 2023

@author: Kevin
"""

def promedio(parcial1, parcial2, parcial3):
    print("primer parcial: ", parcial1)
    print("segundo parcial: ", parcial2)
    print("tercer parcial: ", parcial3)
    resultado=(parcial1+parcial2+parcial3)/3
    return resultado
print("El promedio de los 3 parciales es: ","{:.2f}".format(promedio(15.45,12.25,15.68)))
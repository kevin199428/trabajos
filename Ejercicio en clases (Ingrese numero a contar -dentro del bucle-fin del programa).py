# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 19:30:20 2023

@author: Kevin
"""

num_con=input("ingrese el # al que debo contar: ")
num_con=int(num_con)
contador=1
print("antes del while")
while(True):
    print(contador)
    contador+=1
    if contador>num_con:
        break
    print("dentro del bucle")
print("fin del programa")
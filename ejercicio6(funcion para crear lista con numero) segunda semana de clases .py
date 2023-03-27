# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 19:46:58 2023

@author: Kevin
"""

def crealista(n):
    lista=[]
    for item in range(1,n+1):
        lista.append(item)
    return lista

resultado=crealista(10)
print(resultado)
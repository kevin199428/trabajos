# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 20:21:34 2023

@author: Kevin
"""

lista=["R1","R2","R3",
       "S1","S2","S3"]
print(len(lista))
"""

print(lista[0])
print(lista[5])
"""
for item in lista:
    if "R" in item:
       print(item,end=" * ")
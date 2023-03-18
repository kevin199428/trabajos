# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:46:51 2023

@author: Kevin
"""

age = int(input("Ingrese su edad: "))
if age >=0 and age <=5:
    print("Primeros años")
elif age >=6 and age <=11:
    print("Infante")
elif age >=12 and age <=18:
    print("adolescente")
elif age >=19 and age <=26:
    print("jovenes")
elif age >=27 and age <=59:
    print("adulto")
elif age >=60:
    print("vejez")
else:
    print("no ha nacido")
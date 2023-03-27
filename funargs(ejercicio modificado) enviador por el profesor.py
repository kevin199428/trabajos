# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:05:45 2021

@author: Juan Carlos
*arg

"""

def suma(*a):
    print("\nTipo de datos del argumento:",
         type(a))
    sum = 0
    for n in a:
        sum +=n
        #sum=sum+n

    print("Suma:",sum)

suma(7)
suma(10)
suma(33,56)
suma(41,52,68,79)
suma(15,22,30,59,66)
suma(110,28,35,56,67,17,38,99,140)
suma(166,220,334,551,666,777,881,920,180,119,172,133,147)
suma(10,28,37,56,64,72,87,99,101,121,132,413,145,157,116,137)

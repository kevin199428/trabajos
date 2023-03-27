# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 22:07:27 2021

@author: Juan Carlos

"""
def keyw(**datos):
    print("\nTipo de datos del argumento:",
          type(datos))

    for key, value in datos.items():
        print("{} is {}".format(key,value))

keyw(Firstname="Davis", 
     Lastname="Segarra", 
     Age=23, 
     Phone=959737322)
keyw(Firstname="Victor", 
     Lastname="Iperty",
     Email="victor.perty@nomail.com",
     Country="España", 
     Age=65, 
     Phone=961324578)
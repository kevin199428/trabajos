# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 19:31:22 2023

@author: Kevin
"""

acl=int(input("Ingrese el # de ACL"))
if acl >=1 and acl <=99:
    print("La ACL ES estandar")
elif acl >=100 and acl <=199:
    print("La ACL es extendida")
else:
    print("El dato ingresado no es un ACL")
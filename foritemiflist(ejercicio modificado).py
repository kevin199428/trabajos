# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:29:30 2020

@author: Juan Carlos
"""
switches=[]
devices=["M1","M2","M3",
         "X1","X2","X3",
         "X4","X5"]
for i in devices:
    if "X" in i:
        switches.append(i)
print (switches)
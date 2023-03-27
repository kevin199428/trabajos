# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:29:30 2020

@author: Juan Carlos
"""
router=[]
switches=[]
devices=["Q1","Q2","Q3","P1","P2","HT1"]
for a in devices:
    if "Q" in a:
        router.append(a)
    else:
        switches.append(a)
print(switches)
print(router)        
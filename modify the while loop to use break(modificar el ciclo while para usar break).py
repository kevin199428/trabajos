# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 14:39:02 2023

@author: Kevin
"""

while "true":
   x=input("enter a number to count to: ")
   if x == 'q' or x == 'quit':
        break

x=int(x)
y=1
while "true":
   print(y)
   y=y+1
   if y>x:
    break
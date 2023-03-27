# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 16:54:25 2023

@author: Kevin
"""

def Fibonacci(n):
    a, b =0,1
    while a <= n:
        print(a, end=' ')
        c=a+b
        a=b
        b=c
        #a, b = b, a+b
    print()
Fibonacci(8)
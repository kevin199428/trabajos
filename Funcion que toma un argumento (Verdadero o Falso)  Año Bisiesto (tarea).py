# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 02:28:19 2023

@author: Kevin
"""

def isYearLeap(year):
    """
    Esta función toma un argumento (un año) y devuelve Verdadero si el año es bisiesto o Falso de lo contrario.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
testData = [1900, 2000, 2016, 1987]
testResults = [False, True, True, False]

for i in range(len(testData)):
    yr = testData[i]
    print(yr, "->", end="")
    result = isYearLeap(yr)
    if result == testResults[i]:
        print("OK")
    else:
        print("Failed")
        
    
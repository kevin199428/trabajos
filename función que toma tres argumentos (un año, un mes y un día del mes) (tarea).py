# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 02:41:36 2023

@author: Kevin
"""

def isYearLeap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False


def daysInMonth(year, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        if isYearLeap(year):
            return 29
        else:
            return 28
    else:
        return None


def dayOfYear(year, month, day):
    if month < 1 or month > 12 or day < 1 or day > daysInMonth(year, month):
        return None
    else:
        days = day
        for m in range(1, month):
            mdays = daysInMonth(year, m)
            if mdays == None:
                return None
            days += mdays
        return days


# Test Cases
print(dayOfYear(2000, 12, 31)) # 366
print(dayOfYear(2022, 2, 29)) # None
print(dayOfYear(2022, 13, 1)) # None
print(dayOfYear(2022, 3, 32)) # None
print(dayOfYear(2022, 4, 15)) # 105

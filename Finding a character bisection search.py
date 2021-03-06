# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 22:03:54 2021

@author: dell
"""


def isIn(char, aStr):
    if aStr=='':
        return False
    if len(aStr) == 1:
        return char == aStr
    elif char == aStr[len(aStr)//2]:
        return True
    elif char < aStr[len(aStr)//2]:
        return isIn(char, aStr[:len(aStr)//2]
    elif char > aStr[len(aStr)//2]:
        return isIn(char, aStr[len(aStr)//2:])
print(isIn('w', 'abcdefgklost') )
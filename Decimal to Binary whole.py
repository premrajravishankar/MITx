# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 09:48:53 2021

@author: dell
"""
num = 19
if num<0:
    isNeg = True
    num= abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num> 0:
    result = str(num%2) + result
    num = num // 2
if isNeg:
    result = '-' +result
    
print('Binary representation is ' + result)
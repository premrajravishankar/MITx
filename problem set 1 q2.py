# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 06:22:17 2021

@author: dell
"""

s = 'booobobob'
counter= 0
index = 0
for i in s:
    if i == 'b':
        if s[index:index+3] == 'bob':
            counter += 1
    index += 1
print('Number of times bob occurs is: '+str(counter))
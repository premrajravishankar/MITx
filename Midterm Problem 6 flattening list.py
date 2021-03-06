# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 03:48:20 2021

@author: dell
"""

new = []
def flatten(aList):
    for i in aList:
        if type(i) == list:
            flatten(i)
        else:
            new.append(i)
    return new
print(flatten([[1,'a',['cat'],2],[[[3],4],'dog'],4,5]))
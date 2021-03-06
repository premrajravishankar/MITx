# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 09:53:37 2021

@author: dell
"""


def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    oddTup=()
    i=0
    while  i < len(aTup):
        if i%2 == 0:
            oddTup = oddTup + (aTup[i],)
        i += 1
    return oddTup
s = (1,2,3,4,5,6,'one', 5,6, 'two', ('Three','nine','ten'),('po','mayire'))
print(oddTuples(s))
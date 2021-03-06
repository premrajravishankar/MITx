# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 22:29:30 2021

@author: dell
"""


def fibonacci_efficient(n, d):
    if n in d:
        return d[n]
    else:
        d[n] = fibonacci_efficient(n-1, d) + fibonacci_efficient(n-2, d)
        return d[n]
    
d = {1:1, 2:2}
print(fibonacci_efficient(6, d))
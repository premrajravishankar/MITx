# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 02:43:54 2021

@author: dell
"""
def polysum(n, s):
    '''
    

    Parameters
    ----------
    n : Number of sides takes float
    s : Length of each side in the polygon.
    
    
        DESCRIPTION: This function finds the area and square of perimeter which is added and returned!!

    Returns: Sum of area and square of perimeter..
    -------
    None.

    '''
    import math 
    area = (0.25* n * (s**2))/math.tan(math.pi/n)
    perimeter = n * s
    return round(area + perimeter ** 2, 4)

print(polysum(4, 5))
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 20:16:08 2021

@author: dell
"""


x = int(input('Enter an integer : '))
ans = 0
while ans ** 3 < abs(x):
    ans = ans + 1
if ans ** 3 != abs(x):
    print(str(x)+' is not a perfect cube!!')
else:
    if ans < 0:
        ans = -ans
    print('Cube root of '+str(x)+' is '+str(ans))
    


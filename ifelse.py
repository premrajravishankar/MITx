# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 21:32:12 2021

@author: dell
"""





x = int(input("Enter an integer : "))

if x%2 == 0:
    print('')
    print(' Even!!')
    if x%3 == 0:
        print('\n The number is divisible by 2 and 3!!')
    else:
        print('\n The number is not divisibleby 3!!')
    
else:
    print('')
    print(' Odd!!')
    if x%3 == 0:
        print('\n The number is divisible by 3!!')
    else:
        print('\n The number is not divisibleby 3!!')
    
y = float(input("Enter value for y : "))

if x == y:
    print("\n x and y are equal!!")
elif x>y:
    print('\n x is greater than y!!')
else:
    print('/n y is greater than x!!')
print("\n Thanks!!")
    
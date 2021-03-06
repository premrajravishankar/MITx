# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 22:32:31 2021

@author: dell
"""


cube = 29
epsilon = 0.01
guess = 0.0
# increment= 0.0001
# increment= 0.001
increment= 0.01 
num_guesses = 0
# while abs(guess **3 - cube)>= epsilon:
while abs(guess **3 - cube)>= epsilon and guess <= cube:
    guess += increment
    num_guesses += 1
print(f'The number of guesses is {num_guesses}!!')
if abs(guess ** 3 -cube)>= cube:
    print(f'Failed on cube root of {cube}!!')
else:
    print(f'The number {guess} is close to the cube root of {cube}')
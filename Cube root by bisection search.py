# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 08:52:37 2021

@author: dell
"""


# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 08:44:48 2021

@author: dell
"""


x = 25
epsilon = 0.01
numGuesses = 0
low = 1.0
high = x
ans = (high+low)  / 2.0

while abs(ans **3-x) >= epsilon:
    print('low = '+ str(low)+' High = '+str(high)+' Answer = '+str(ans))
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high+low) / 2.0
print('Number of Guesses =  '+str(numGuesses))
print(str(ans)+ ' is close to the square root of '+str(x)+'!!')
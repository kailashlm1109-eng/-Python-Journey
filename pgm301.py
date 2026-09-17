# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 10:53:45 2026
extract only unique values
@author: KAILASH L M
"""
import random
a=[]
n=int(input("Enter a no. of elements in a list:"))
for j in range(n):
    x=random.randint(-100,100)
    a.append(x)
print(a)
b=[]
for j in a:
    if j in b:
        pass
    else:
         b.append(j)
print(b)
         

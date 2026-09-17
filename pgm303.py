# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:21:15 2026
store a frequency count as list
@author: KAILASH L M
"""
import random
l=[]
n=int(input("Enter a no. of elements in a list:"))
for j in range(n):
    x=random.randint(-10,10)
    l.append(x)
print(l)
u=[]
for j in l:
    if j in u:
        pass
    else:
         u.append(j)
print(u)
c=[]
for k in u:
    y=l.count(k)
    c.append(y)
print(c)

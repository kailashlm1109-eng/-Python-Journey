# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 11:05:11 2026
Frequency count of value of list
@author: KAILASH L M
"""
import random
a=[]
n=int(input("Enter a no. of elements in a list:"))
for j in range(n):
    x=random.randint(-10,10)
    a.append(x)
print(a)
b=[]
for j in a:
    if j in b:
        pass
    else:
         b.append(j)
for k in b:
    c=a.count(k)
    print("Count of",k,"is",c)
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 10:37:21 2026
find the second biggest
@author: KAILASH L M
"""
import random
a=[]
n=int(input("Enter a no. of elements in a list:"))
for j in range(n):
    x=random.randint(-100,100)
    a.append(x)
print(a)
p=max(a)
b=0
for j in range(n):
    if a[j]!=p:
        b=j if a[j]>a[b] else b
print("The second biggest element:",a[b])

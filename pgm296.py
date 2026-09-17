# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 10:35:12 2026
interchange biggest and smallest
@author: KAILASH L M
"""
import random
a=[]
n=int(input("Enter a no. of elements in a list:"))
for j in range(n):
    x=random.randint(-100,100)
    a.append(x)
print(a)
b=max(a)
s=min(a)
i=a.index(b)
j=a.index(s)
a[i]=s
a[j]=b
print(a)
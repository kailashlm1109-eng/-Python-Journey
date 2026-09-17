# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 10:40:33 2026
inter change second biggest and second smallest
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
q=min(a)
b=0
s=0
for j in range(n):
    if a[j]!=p:
        b=j if a[j]>a[b] else b
    if a[j]!=q:
        s=j if a[j]<a[s]else s
x=a[b]
a[b]=a[s]
a[s]=x
print(a)

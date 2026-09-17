# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:56:18 2026
reverse
@author: KAILASH L M
"""
import random
n=int(input("Enter a number of value in a list:"))
a=[]
b=[]
i=1
while i<=n:
    x=random.randint(-100,100)
    a.append(x)
    i=i+1
print(a)
j=n-1
while j>=0:
    b.append(a[j])
    j=j-1
print("Reverse:",b)

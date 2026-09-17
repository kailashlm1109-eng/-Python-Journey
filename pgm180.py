# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:55:16 2026
Alternative elements
@author: KAILASH L M
"""
import random
n=int(input("Enter a number of value in a list:"))
a=[]
i=1
while i<=n:
    x=random.randint(-100,100)
    a.append(x)
    i=i+1
print(a)
j=0
while j<n:
    print(a[j])
    j=j+2

# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:03:23 2026
index of biggest and smallest
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
b=-100
s=100
j=0
while j<n:
    if a[j]>b:
        b=a[j]
    elif a[j]<s:
        s=a[j]
    else:
        pass
    j=j+1
print("Biggest:",b)
print("Smallest:",s)



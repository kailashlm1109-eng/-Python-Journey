# -*- coding: utf-8 -*-
"""
Created on Sat May 16 10:50:07 2026
list of n random number 1 by 1
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
j=0
while j<n:
    print(a[j])
    j=j+1
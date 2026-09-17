# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:05:00 2026

@author: KAILASH L M
"""
import random
a=[]
n=int(input("Enter a value of n:"))
i=1
while i<=n:
    x=random.randint(-100,100)
    a.append(x)
    i=i+1
print(a)

# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:36:09 2026
Sort the list
@author: KAILASH L M
"""
import random
l=[]
n=int(input("Enter a no. of elements in a list:"))
for j in range(n):
    x=random.randint(-10,10)
    l.append(x)
print("list:",l)
l.sort()
print("Sorted list:",l)

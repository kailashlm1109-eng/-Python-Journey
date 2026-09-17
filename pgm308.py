# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:44:32 2026
sort the list to another list
@author: KAILASH L M
"""
import random
l=[]
n=int(input("Enter a no. of elements in a list:"))
for j in range(n):
    x=random.randint(-10,10)
    l.append(x)
print("list:",l)
s=sorted(l)
print("Sorted list:",s)


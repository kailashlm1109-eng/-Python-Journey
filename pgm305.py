# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:15:52 2026
insert a element in a list
@author: KAILASH L M
"""
import random
l=[]
n=int(input("Enter a no. of elements in a list:"))
for j in range(n):
    x=random.randint(-10,10)
    l.append(x)
print("list:",l)
a=int(input("Enter a index of element to be added:"))
b=int(input("Enter a value to be added:"))
l.insert(a,b)
print(l)

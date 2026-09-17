# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 11:43:02 2026
delete a element from a list
@author: KAILASH L M
"""
import random
l=[]
n=int(input("Enter a no of leement in a list:"))
for i in range(n):
    x=random.randint(-100,100)
    l.append(x)
print(l)
j=int(input("Enter a element to delete:"))
l.remove(j)
print(l)
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 10:38:23 2026
count of unique value in a list
@author: KAILASH L M
"""
import random
n=int(input("Enter no. of element in a list:"))
l=[random.randint(-100,100) for i in range(n)]
print(l)
s=set(l)
print(s)
c=[]
for i in s:
    c.append(l.count(i))
print(c)



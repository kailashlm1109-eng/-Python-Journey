# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 10:40:36 2026
Higgest occourence of the list
@author: KAILASH L M
"""
import random
n=int(input("Enter no. of element in a list:"))
l=[random.randint(-100,100) for i in range(n)]
print(l)
s=set(l)
u=list(s)
print(u)
c=[]
for j in u:
    c.append(l.count(j))
print(c)
x=max(c)
print("Higgest occourence of list:",x)
print("Higgest occoured value:",u[c.index(x)])
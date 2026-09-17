# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 09:51:20 2026
Highest and lowest occourence of the list
@author: KAILASH L M
"""
import random
l=[]
n=int(input("Enter a no. of elements in a list:"))
for j in range(n):
    x=random.randint(-10,10)
    l.append(x)
print("list:",l)
u=[]
for j in l:
    if j in u:
        pass
    else:
         u.append(j)
print("unique list:",u)
c=[]
for k in u:
    y=l.count(k)
    c.append(y)
print("Frequency count:",c)
m=max(c)
n=min(c)
p=c.index(m)
q=c.index(n)
print("Highest Occourance of the list:",u[p])
print("Lowest Occourence of the list:",u[q])


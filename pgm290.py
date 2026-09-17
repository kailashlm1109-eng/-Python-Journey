# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 10:24:20 2026
difference
@author: KAILASH L M
"""
import random
m=[]
n=[]
for i in range(3):
    a=[]
    for j in range(3):
        x=random.randint(-100,100)
        a.append(x)
    m.append(a)
    b=[]
    for k in range(3):
        y=random.randint(-100,100)
        b.append(y)
    n.append(b)
print(m)
print(n)
s=[]
for r in range(3):
    p=[]
    for c in range(3):
        z=m[r][c]-n[r][c]
        p.append(z)
    s.append(z)
    
print(s)

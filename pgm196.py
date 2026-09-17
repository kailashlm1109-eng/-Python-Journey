# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:47:09 2026
difference of 2 matrices
@author: KAILASH L M
"""
import random
m=[]
i=1
while i<=3:
    j=0
    a=[]
    while j<3:
        x=random.randint(-100, 100)
        a.append(x)
        j=j+1
    m.append(a)
    i=i+1
print(m)
n=[]
k=1
while k<=3:
    l=0
    b=[]
    while l<3:
        y=random.randint(-100, 100)
        b.append(y)
        l=l+1
    n.append(a)
    k=k+1
print(n)
r=0
s=[]
while r<3:
    p=[]
    c=0
    while c<3:
        t=m[r][c]-n[r][c]
        p.append(t)
        c=c+1
    s.append(p)
    r=r+1
print("SUM:",s)


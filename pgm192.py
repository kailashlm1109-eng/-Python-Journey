# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:39:17 2026

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
r=0
while r<3:
    c=0
    s=0
    while c<3:
        s=s+m[r][c]
        c=c+1
    print("sum of row:",s)
    r=r+1
    

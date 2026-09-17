# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:47:47 2026
biggest of row
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
    b=-100
    c=0
    while c<3:
        if m[r][c]>b:
            b=m[r][c]
        else:
            pass
        c=c+1
        print("BIG:",b)
    r=r+1



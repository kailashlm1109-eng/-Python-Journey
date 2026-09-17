# -*- coding: utf-8 -*-
"""
Created on Mon May 18 11:34:48 2026
matrices print row by row
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
k=0
while k<3:
    print(m[k])
    k=k+1

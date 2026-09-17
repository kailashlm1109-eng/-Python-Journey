# -*- coding: utf-8 -*-
"""
Created on construct 3*3 matrices
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
        
    

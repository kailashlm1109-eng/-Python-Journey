# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:38:24 2026
Sum of two matrices
@author: KAILASH L M
"""
import random
def matric():
    l=[[random.randint(-100,100) for i in range(3)]for j in range(3)]
    return l
def matric_sum(x,y):
    s=[[x[r][c]+y[r][c] for c in range(3)]for r in range(3)]
    return s
def show(y):
    for r in y:
        print(r)
    print()
#Main
m1=matric()
show(m1)
m2=matric()
show(m2)
s=matric_sum(m1,m2)
print("SUM:")
show(s)
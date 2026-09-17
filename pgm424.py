# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:33:43 2026
Find the sum of two matic
@author: KAILASH L M
"""
import random
def matric():
    l=[[random.randint(-100,100) for i in range(3)]for j in range(3)]
    return l
def row_sum(x):
    for r in x:
        print("Sum of row:",sum(r))
def show(y):
    for r in y:
        print(r)
#main
m1=matric()
show(m1)
row_sum(m1)

m2=matric()
show(m2)
row_sum(m2)

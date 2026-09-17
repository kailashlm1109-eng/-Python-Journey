# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:29:39 2026
construct a 3 by 3 matrices and print into another function
@author: KAILASH L M
"""
import random
def matric():
    l=[[random.randint(-100,100) for i in range(3)]for j in range(3)]
    return l
def show_matric(x):
    for p in x:
        print(p)
#main
m1=matric()
show_matric(m1)
print()

m2=matric()
show_matric(m2)
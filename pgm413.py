# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:31:46 2026
Biggest and smallest of argument passed
@author: KAILASH L M
"""
def bigsmall(*x):
    b=-10000
    s=10000
    for i in x:
        b=i if b<i else b
        s=i if s>i else s
    print("Biggest:",b)
    print("Smallest:",s)
#main
bigsmall(6,55,86,64,77,65,45)
bigsmall(77,35,1,88,15)

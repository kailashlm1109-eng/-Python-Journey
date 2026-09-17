# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:28:42 2026
sum of the element of argument passed
@author: KAILASH L M
"""
def add(*x):
    s=0
    for i in x:
        s+=i
    print("SUM:",s)
#main
add(77,98,36,7,43,35)
add(57,35,79,43,66,56,79)
add(7,65,9,4,6,67)

# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:38:44 2026
product of two number using default argument
@author: KAILASH L M
"""
def prod(a=10,b=20):
    p=a*b
    return p
#main
p1=prod()
p2=prod(30)
p3=prod(30,11)
print("Product 1:",p1)
print("Product 2:",p2)
print("Product 3:",p3)

# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:03:09 2026
product of two number using inner function
@author: KAILASH L M
"""
def calculate():
    def prod(a,b):
        return a*b
    i=float(input("Enter a number 1:"))
    j=float(input("Enter a number 2:"))
    m=prod(i,j)
    return m
#main
p1=calculate()
print("Product 1:",p1)
p2=calculate()
print("Product 2:",p2)
p3=calculate()
print("Product 3:",p3)
    

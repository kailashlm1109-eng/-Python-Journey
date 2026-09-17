# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:46:04 2026
Product of two real numbers by getting the function form inner function
@author: KAILASH L M
"""
def calculate(a,b):
    def prod():
        return a*b
    return prod
#main
x=calculate(86,68)
y=x()
print("Product 1:",y)
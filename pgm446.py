# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:40:13 2026
Find the sum of two integer by return function from inner function
@author: KAILASH L M
"""
def calculate(a,b):
    def add():
        return a+b
    return add
#main
x=calculate(5,6)
y=x()
print("SUM 1:",y)
x1=calculate(52,39)
y1=x1()
print("SUM 2:",y1)

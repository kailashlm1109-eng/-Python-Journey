# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:51:21 2026
Find sum by passing each data in each inner and outer function
@author: KAILASH L M
"""
def calculate(a):
    def add(b):
        return a+b
    return add
#main
addition=calculate(5)
x=addition(10)
y=addition(20)
z=addition(30)
print("Sum 1:",x)
print("Sum 2:",y)
print("Sum 3:",z)

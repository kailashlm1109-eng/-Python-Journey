# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:54:56 2026
print the Multiplication table(closure function)
@author: KAILASH L M
"""
def calculate(a):
    def table(b):
        return a*b
    return table
#main
prod=calculate(5)
for i in range(1,11):
    x=prod(i)
    print(i,"*",5,"=",x)
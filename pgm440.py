# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 10:59:27 2026
Find the sum of two integer using inner function
@author: KAILASH L M
"""
def calculate():
    def add(a,b):
        return a+b
    i=int(input("Enter a number 1:"))
    j=int(input("Enter a number 2:"))
    a=add(i,j)
    return a
#Main
s1=calculate()
print("SUM:1",s1)
s2=calculate()
print("Sum2:",s2)
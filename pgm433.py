# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 10:19:45 2026
sum of two int pass func to fucn
@author: KAILASH L M
"""
def sum(a,b):
    return a+b
def calculate(f):
    x=int(input("Enter a number 1:"))
    y=int(input("Enter a number 2:"))
    c=f(x,y)
    return c
#main
c1=calculate(sum)
print("SUM:",c1)
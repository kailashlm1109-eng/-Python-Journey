# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 10:22:25 2026
sum of two numbe by func
@author: KAILASH L M
"""
def sum(a,b):
    return a+b
def calculate(f,i,j):
    c=f(i,j)
    return c
#main
x=int(input("Enter a number 1:"))
y=int(input("Enter a number 2:"))
c1=calculate(sum,x,y)
print("SUM:",c1)

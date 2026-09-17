# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 10:24:16 2026
bigg of three by pass func and data to another func
@author: KAILASH L M
"""
def big(x,y,z):
    b=x if x>y and x>z else y if y>z else z
    return b
def calculate(f,i,j,k):
    m=f(i,j,k)
    return m
#main
p=int(input("Enter number1:"))
q=int(input("Enter a number2:"))
r=int(input("Enter a number3:"))
b1=calculate(big, p, q, r)
print("Big:",b1)

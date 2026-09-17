# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:06:53 2026
biggest of three
@author: KAILASH L M
"""
def calculate():
    def big(a,b,c):
        m=max(a,b,c)
        return m
    i=int(input("Enter number 1:"))
    j=int(input("Enter number 2:"))
    k=int(input("Enter number 3:"))
    b=big(i,j,k)
    return b
#main
b1=calculate()
print("Biggest 1:",b1)
b2=calculate()
print("Biggest 2:",b2)
b3=calculate()
print("Biggest 3:",b3)

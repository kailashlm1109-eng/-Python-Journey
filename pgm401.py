# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:07:16 2026
Biggest of three numbers
@author: KAILASH L M
"""
def bigg(a,b,c):
    m=a if a>b and a>c else b if b>c else c
    return m
#main
x=int(input("Enter number:"))
y=int(input("Enter number:"))
z=int(input("Enter number:"))
i=bigg(x,y,z)
print("Biggest:",i)
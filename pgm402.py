# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 11:19:29 2026
biggest and smallest of three numbers
@author: KAILASH L M
"""
def bigsmall(a,b,c):
    m=a if a>b and a>c else b if b>c else c
    n=a if a<b and a<c else b if b<c else c
    return m,n
#main
x=int(input("Enter a number:"))
y=int(input("Enter a number:"))
z=int(input("Enter a number:"))
i,j=bigsmall(x,y,z)
print("Biggest:",i)
print("Smallest:",j)


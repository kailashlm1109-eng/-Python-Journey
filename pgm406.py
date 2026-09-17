# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:15:35 2026
biggest and smallest by keyword argument
@author: KAILASH L M
"""
def bigsmall(a,b,c):
    m=a if a>b and a>c else b if b>c else c
    n=a if a<b and a<c else b if b<c else c
    return m,n
#main
b1,s1=bigsmall(a=68,b=98,c=79)
b2,s2=bigsmall(a=65,b=79,c=35)
print("Biggest 1:",b1)
print("Smallest 1:",s1)
print("Biggest 2:",b2)
print("Smallest 2:",s2)

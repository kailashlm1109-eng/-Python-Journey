# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:44:14 2026
biggest and smallest of 3 numbers (default arguments)
@author: KAILASH L M
"""
def bigsmall(a=10,b=20,c=30):
    x=a if a>b and a>c else b if b>c else c
    y=a if a<b and a<c else b if b<c else c
    return x,y
#main
b1,s1=bigsmall()
b2,s2=bigsmall(35)
b3,s3=bigsmall(40,13)
b4,s4=bigsmall(5,10,15)
print("Biggest 1:",b1)
print("Smallest 1:",s1)
print("Biggest 2:",b2)
print("Smallest 3:",s2)
print("Biggest 3:",b3)
print("Smallest 3:",s3)
print("Biggest 4:",b4)
print("Smallest 4:",s4)

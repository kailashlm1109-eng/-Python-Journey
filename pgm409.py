# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:40:59 2026
biggest of 3 numbers using default argument
@author: KAILASH L M
"""
def big(a=10,b=20,c=30):
    x=a if a>b and a>c else b if b>c else c
    return x
#main
b1=big()
b2=big(35)
b3=big(40,13)
b4=big(5,10,15)
print("Biggest 1:",b1)
print("Biggest 2:",b2)
print("Biggest 3:",b3)
print("Biggest 4:",b4)

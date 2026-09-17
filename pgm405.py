# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:12:57 2026
Biggest of three number using keyword arguments
@author: KAILASH L M
"""
def big(a,b,c):
    d=a if a>b and a>c else b if b>c else c
    return d
#main
m1=big(c=68,a=65,b=572)
print("Biggest 1:",m1)
m2=big(b=76,a=98,c=97)
print("Biggest 2:",m2)
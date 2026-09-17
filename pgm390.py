# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:35:06 2026
store text & Frequency count in dictionary
@author: KAILASH L M
"""
s=input("Enter a string:")
l=s.split()
print("LIST:",l)
x=set(l)
u=list(x)
print("UNIQUE:",u)
d={}
for i in u:
    d[i]=l.count(i)
print(d)


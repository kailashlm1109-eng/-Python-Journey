# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:39:21 2026
Higgest occourence of the word
@author: KAILASH L M
"""
s=input("Enter a string:")
l=s.split()
print(l)
x=set(l)
u=list(x)
print(u)
f=[]
for i in u:
    f.append(l.count(i))
print(f)
m=max(f)
print("Higgest Occourence:",m)
print("Higgest Occoured text:",u[f.index(m)])

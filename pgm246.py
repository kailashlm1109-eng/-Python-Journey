# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:07:48 2026
biggest and smallest
@author: KAILASH L M
"""
b=0
s=0
for i in range(10):
    n=int(input("Enter a number:"))
    b=n if n>b else b
    s=n if s<n else s
print("The Biggest of given numbers:",b)
print("The Smallest of given numbers:",s)

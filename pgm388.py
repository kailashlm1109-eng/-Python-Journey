# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 10:56:54 2026
print the unique words of a string
@author: KAILASH L M
"""
s=input("Enter a sentence:")

a=s.split()
x=set(a)
u=list(x)
print(u)

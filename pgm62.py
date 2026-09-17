# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:29:31 2026
Smallest of 3 integer(ternery)
@author: KAILASH L M
"""
a=int(input("Enter value A:"))
b=int(input("Enter value B:"))
c=int(input("Enter value C:"))
d=a if a<b else b
e=c if c<d else d
print(e,"is Smallest")


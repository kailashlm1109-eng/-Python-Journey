# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 11:33:54 2026
Smallest of 3 (ternery nested)
@author: KAILASH L M
"""
a=int(input("Enter value A:"))
b=int(input("Enter value B:"))
c=int(input("Enter value C:"))
d=a if a<c else c if a<b else b if b<c else c
print(d,"is Smallest")

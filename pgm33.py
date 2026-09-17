# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:38:51 2026
smallest of 3 integers
@author: KAILASH L M
"""
a=int(input("Enter a value A:"))
b=int(input("Enter a value B:"))
c=int(input("Enter a value C:"))
if a<b:
    if a<c:
        print("A is SMALLEST")
    else:
        print("C is SMALLEST")
else:
    if b<c:
        print("B is SMALLEST")
    else:
        print("C is SMALLEST")

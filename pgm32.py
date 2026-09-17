# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:34:13 2026
Biggest fo 3 integers
@author: KAILASH L M
"""
a=int(input("Enter a value A:"))
b=int(input("Enter a value B:"))
c=int(input("Enter a value C:"))
if a>b:
    if a>c:
        print("A is BIGGEST")
    else:
        print("C is BIGGEST")
else:
    if b>c:
        print("B is BIGGEST")
    else:
        print("C is BIGGEST")
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:55:05 2026
digit or not unicode
@author: KAILASH L M
"""
a=input("Enter a character:")
x=ord(a)
if x>=48 and x<=57:
    print(a,"is DIGIT")
else:
    print(a,"is not DIGIT")

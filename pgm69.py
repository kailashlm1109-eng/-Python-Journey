# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 10:56:09 2026
upper/lower/digit/spl char(unicode)
@author: KAILASH L M
"""
a=input("Enter a character:")
x=ord(a)
if x>=65 and x<=90:
    print(a,"is UPPER")
elif x>=97 and x<=122:
    print(a,"is LOWER")
elif x>=48 and x<=57:
    print(a,"is digit")
else:
    print(a,"is special character")
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:54:34 2026
upper/lower/digit/spl character
@author: KAILASH L M
"""
a=(input("Enter a character:"))
if a>='A' and a<='Z':
    print(a,"is uppercase character")
elif a>='a' and a<='z':
    print(a,"is a lower case letter")
elif a>='0' and a<='9':
    print(a,"is a digit")
else:
    print(a,"is a special character")

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:03:52 2026
flip the char
@author: KAILASH L M
"""
a=input("Enter a character:")
x=ord(a)
if x>=65 and x<=90:
    y=x+32
    z=chr(y)
    print("The lower=",z)
elif x>=97 and x<=122:
    y=x-32
    z=chr(y)
    print("The =",z)

else:
    print("Invalid input")

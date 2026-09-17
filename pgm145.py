# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:40:18 2026
smallest of 10 integers
@author: KAILASH L M
"""
x=99999
i=1
while i<=10:
    a=int(input("Enter a number:"))
    if a<x:
        x=a
    else:
        pass
    i=i+1   
print("The Smallest of given 10 integers:",x)


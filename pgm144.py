# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:35:39 2026
biggest of 10 integers
@author: KAILASH L M
"""
x=0
i=1
while i<=10:
    a=int(input("Enter a number:"))
    if x<a:
        x=a
    else:
        x=x
    i=i+1
print("The Biggest of given 10 integers:",a)

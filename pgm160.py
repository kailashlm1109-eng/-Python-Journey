# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:33:22 2026
last n character
@author: KAILASH L M
"""
s=input("Enter a string:")
n=int(input("Enter a postion of string:"))
s1=''
x=len(s)
i=x-n
while i<x:
    s1=s1+s[i]
    i=i+1
print(s1)

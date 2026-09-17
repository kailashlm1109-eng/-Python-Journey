# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:28:10 2026
copy all character from nth position
@author: KAILASH L M
"""
s=input("Enter a string:")
n=int(input("Enter a postion of string:"))
s1=''
x=len(s)
i=0
while i<x:
    n=ord(s[i])
    s1=s1+s[i]
    i=i+1
print(s1)

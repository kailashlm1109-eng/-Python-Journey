# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:39:10 2026
First n character from right
@author: KAILASH L M
"""
s=input("Enter a string:")
n=int(input("Enter a postion of string:"))
s1=''
l=-n
i=-1
while i>l:
    s=s1+s[i]
    i=i-1
print(s1)

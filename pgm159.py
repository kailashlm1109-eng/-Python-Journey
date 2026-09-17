# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:31:06 2026
copy n character fron nth position
@author: KAILASH L M
"""
s=input("Enter a string:")
m=int(input("Enter the position of string"))
n=int(input("Enter a postion of string:"))
s1=''
i=m
while i<m+n:
    s1=s1+s[i]
    i=i+1
print(s1)


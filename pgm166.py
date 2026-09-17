# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:48:00 2026
n char from n position
@author: KAILASH L M
"""
s=input("Enter a string:")
m=int(input("Enter the position of string"))
n=int(input("Enter a postion of string:"))
l=-m-n
s1=''
i=-m
while i>l:
    s1=s1+s[i]
    i=i-1
print(s1)

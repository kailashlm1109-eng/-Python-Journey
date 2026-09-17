# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:20:45 2026
Flip the string
@author: KAILASH L M
"""
s=input("Enter a string:")
a=len(s)
s1=''
i=0
while i<a:
    n=ord(s[i])
    if n>=65 and n<=90:
        l=ord(s[i])+32
        s1=s1+chr(l)  
    elif n>=97 and n<=122:
        u=ord(s[i])-32
        s1=s1+chr(u)
    else:
        s1=s1+s[i]
    i=i+s
print(s1)

# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:18:00 2026
lower case
@author: KAILASH L M
"""
s=input("Enter a string:")
a=len(s)
s1=''
i=0
while i<a:
    n=ord(s[i])
    if n>=65 and n<=90:
        s1=s1+s[i]

    else:
        l=ord(s[i]+32)
        s1=s1+chr(l)
        
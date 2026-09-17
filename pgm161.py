# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:34:26 2026
Reverse the text
@author: KAILASH L M
"""

s=input("Enter a string:")
s1=''
l=len(s)
i=l-1
while i>=0:
    s1=s1+s[i]
    i=i-1
print(s1)

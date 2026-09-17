# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:35:35 2026
palindrome or not
@author: KAILASH L M
"""
s=input("Enter a string:")
l=len(s)
s1=''
i=l-1
while i>=0:
    s1=s1+s[i]
    i=i-1
if s==s1:
    print("PALINDROME")
else:
    print("NOT PALINDROME")
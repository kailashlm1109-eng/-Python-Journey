# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:17:56 2026
copy n character
@author: KAILASH L M
"""
s=input("Enter a string:")
n=int(input("Enter a no. of character:"))
s1=''
for i in range(n):
    s1+=s[i]
print(s1)
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:20:39 2026
copy all from nth positiob
@author: KAILASH L M
"""
s=(input("Enter a string:"))
n=int(input("Enter a number of string:"))
s1=''
for i in range(n,len(s)):
    s1+=s[i]
print(s1)


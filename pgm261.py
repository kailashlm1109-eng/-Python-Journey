# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:23:23 2026
copy from n char form mth  position
@author: KAILASH L M
"""
s=input("Enter a charactet:")
s1=''
n=int(input("Enter a number:"))
m=int(input("Enter a number:"))
for i in range (m,m+n):
    s1+=s[i]
print(s1)
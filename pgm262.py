# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:25:36 2026
copy last n char
@author: KAILASH L M
"""
s=input("Enter a charactet:")
s1=''
n=int(input("Enter a number:"))
for i in range (-1,-n-1,-1):
    s1+=s[i]
print(s1)


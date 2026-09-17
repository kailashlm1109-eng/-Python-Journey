# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:27:21 2026
Reverse the text
@author: KAILASH L M
"""

s=input("Enter a charactet:")
s1=''
for i in range (-1,-len(s)-1,-1):
    s1+=s[i]
print(s1)

# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:11:58 2026
copy string by deleting vowel
@author: KAILASH L M
"""
s=input("Enter a string:")
s1=''
for i in s:
    if i not in 'AEIOU':
        s1+=i
print(s1)

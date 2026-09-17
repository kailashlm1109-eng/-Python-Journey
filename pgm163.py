# -*- coding: utf-8 -*-
"""
Created on Mon May 11 11:37:45 2026
reverse the text
@author: KAILASH L M
"""
s=input("Enter a string:")
s1=''
l=-len(s)
i=-1
while i>=l:
    s1=s1+s[i]
    i=i-1
print(s1)

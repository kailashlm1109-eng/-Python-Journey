# -*- coding: utf-8 -*-
"""
Created on Thu May 14 10:46:52 2026
last n character(-ve index)
@author: KAILASH L M
"""
s=input("Enter a string:")
n=int(input("Enter a no. of character to be copied:"))
s1=''
l=-len(s)
i=l+n-1
while i>=l:
    s1=s1+s[i]
    i=i-1
print(s1)
    

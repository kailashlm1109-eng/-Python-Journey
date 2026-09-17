# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:22:23 2026
copy last n character of the string
@author: KAILASH L M
"""
s=input("Enter a string:")
n=int(input("Enter a no. of char to be copy:"))
s1=s[len(s)-n:]
print(s1)
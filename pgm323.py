# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:57:01 2026
copy n character from the right edge
@author: KAILASH L M
"""
s=input("Enter a string:")
n=int(input("Enter a no. of character to be copy:"))
s1=s[-1:-n-1:-1]
print(s1)
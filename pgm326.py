# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:06:36 2026
copy last n char of the string
@author: KAILASH L M
"""
s=input("Enter a string:")
n=int(input("Enter a no of character to be copy:"))
s1=s[-(len(s)-n)::-1]
print(s1)

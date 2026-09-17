# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:00:25 2026
copy all character from the mth position(-ve idexing)
@author: KAILASH L M
"""
s=input("Enter a string:")
m=int(input("Enter a position copy from:"))
s1=s[m::-1]
print(s1)

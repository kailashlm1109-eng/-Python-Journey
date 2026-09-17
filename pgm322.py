# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 10:25:56 2026
Palindrom or not
@author: KAILASH L M
"""
s=input("Enter a string:")
s1=s[::-1]
a='PALINDROME' if s==s1 else 'NOT PALINDROME'
print(a)

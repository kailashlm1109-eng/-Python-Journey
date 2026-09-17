# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:03:39 2026
copy n char from the nth position
@author: KAILASH L M
"""
s=input("Enter a string:")
m=int(input("Enter a positon copy from:"))
n=int(input("Enter no. of char to copy:"))
l=len(s)-m
s1=s[-l:-l-4:-1]
print(s1)
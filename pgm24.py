# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:58:26 2026
3 digit numbers (digits)
@author: KAILASH L M
"""
n=int(input("Enter a 3-digit number:"))
a=n%10
x=n//10
b=x%10
c=x//10
print("one's place:",a)
print("ten's place:",b)
print("hundred's place:",c)
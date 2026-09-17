# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:52:30 2026
palindrome or not
@author: KAILASH L M
"""
n=int(input("Enter a 3-digit number:"))
a=n%10
x=n//10
b=x%10
c=x//10
r=(a*100)+(b*10)+c
if r==n:
    print(n,"is a palindrome number")
else:
    print(n,"is not a palindrome number")
    
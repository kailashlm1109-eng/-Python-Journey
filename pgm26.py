# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:05:34 2026
reverse digits
@author: KAILASH L M
"""
n=int(input("Enter a 3-digit number:"))
a=n%10
x=n//10
b=x%10
c=x//10
r=(a*100)+(b*10)+c
print("The reversed number is:",r)

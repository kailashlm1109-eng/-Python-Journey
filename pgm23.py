# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 16:55:38 2026
sun and product of digits
@author: KAILASH L M
"""
n=int(input("Enter a 2-digit number:"))
a=n%10
b=n//10
s=a+b
p=a*b
print("Sum of the digits:",s)
print("Product of the digits:",p)

# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:02:56 2026
sum and product fo 3-digit numbers
@author: KAILASH L M
"""
n=int(input("Enter a 3-digit number:"))
a=n%10
x=n//10
b=x%10
c=x//10
s=a+b+c
p=a*b*c
print("Sum of the digits:",s)
print("Product of the digits:",p)

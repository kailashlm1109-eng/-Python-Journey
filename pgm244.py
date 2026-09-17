# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:04:09 2026
read 10 numbers and find big
@author: KAILASH L M
"""
b=0
for i in range(10):
    n=int(input("Enter a number:"))
    b=n if n>b else b
print("The Biggest of given numbers:",b)
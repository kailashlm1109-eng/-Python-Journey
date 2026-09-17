# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:06:41 2026
read 10 number and small
@author: KAILASH L M
"""
s=0
for i in range(10):
    n=int(input("Enter a number:"))
    s=n if n>s else s
print("The Smallest of given numbers:",s)

# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 09:55:05 2026
Extract only the odd numbers
@author: KAILASH L M
"""
import random
n=int(input("Enter a no. of element in a list:"))
a=[random.randint(-100,100) for i in range(n)]
b=[j for j in a if j%2]
print(a)
print(b)
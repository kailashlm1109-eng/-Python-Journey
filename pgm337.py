# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 10:22:48 2026
constuct a list of student mark modify mark 35-39 as 40
@author: KAILASH L M
"""
import random
n=int(input("Enter a no. of element in a list:"))
r=[random.randint(1,100) for i in range(n)]
print(r)
a=[40 if j>=35 and j<=39 else j for j in r]
print(a)

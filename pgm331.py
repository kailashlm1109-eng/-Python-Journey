# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 11:41:36 2026
construct a list comprehension of n random numbers
@author: KAILASH L M
"""
import random
n=int(input("Enter a no. of element in a list:"))
a=[random.randint(-100,100) for i in range(n)]
print(a)
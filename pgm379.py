# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:20:03 2026
construct a set of n random numbers
@author: KAILASH L M
"""
import random
n=int(input("Enter a no. of element in a set:"))
a={random.randint(-100,100) for i in range(n)}
print(a)

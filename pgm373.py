# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:06:26 2026
construct a set from list of n random numbers
@author: KAILASH L M
"""
import random
n=int(input("Enter no. of element:"))
l=[random.randint(-100,100) for i in range(n)]
a=set(l)
print(a)

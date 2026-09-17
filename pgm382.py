# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 10:31:54 2026
unique value of the list
@author: KAILASH L M
"""
import random
n=int(input("Enter no. of element in a list:"))
l=[random.randint(-100,100) for i in range(n)]
print(l)
s=set(l)
print(s)

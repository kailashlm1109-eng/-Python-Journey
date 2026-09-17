# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 10:34:03 2026
percentage of unique value
@author: KAILASH L M
"""
import random
n=int(input("Enter no. of element in a list:"))
l=[random.randint(-100,100) for i in range(n)]
print(l)
s=set(l)
print(s)
p=(len(s)/len(l))*100
print("Percentage of unique values:",p,'%')

# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 10:44:50 2026
count no of value in a list
@author: KAILASH L M
"""
import random
a=[]
n=int(input("Enter a no. of elements in a list:"))
for j in range(n):
    x=random.randint(-100,100)
    a.append(x)
print(a)
j=int(input("Enter a value to be count:"))
c=a.count(j)
print("Count =",c)

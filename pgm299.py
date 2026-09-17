# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 10:42:52 2026
whether given is  available or not
@author: KAILASH L M
"""
import random
a=[]
n=int(input("Enter a no. of elements in a list:"))
for j in range(n):
    x=random.randint(-100,100)
    a.append(x)
print(a)
j=int(input("Enter a value to check:"))
if j in a:
    print("Available")
else:
    print("Not Available")


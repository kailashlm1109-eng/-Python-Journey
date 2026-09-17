# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:02:11 2026
print n random number -100 to 100
@author: KAILASH L M
"""
import random
n=int(input("Enter a value of n:"))
i=1
while i<=n:
    x=random.randint(-100,100)
    print(x)
    i=i+1



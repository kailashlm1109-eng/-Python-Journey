# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 10:19:28 2026
change even no. as 0
@author: KAILASH L M
"""
import random
n=int(input("Enter a no. of element in a list:"))
r=[random.randint(-50100,100) for i in range(n)]
print(r)
a=[0 if j%2==0 else j for j in r]
print(a)
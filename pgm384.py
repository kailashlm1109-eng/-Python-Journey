# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 10:35:53 2026
count the no. of unique value in a list
@author: KAILASH L M
"""
import random
n=int(input("Enter no. of element in a list:"))
l=[random.randint(-100,100) for i in range(n)]
print(l)
s=set(l)
print(s)
for j in s:
    print("Count of ",j,"-",l.count(j))
    
    



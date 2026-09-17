# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 09:57:25 2026
extract  the single digit 2-digit 3-digit and 4-digit numbers
@author: KAILASH L M
"""
import random
n=int(input("Enter a no. of element in a list:"))
a=[random.randint(1,10000) for i in range(n)]
print(a)
s=[j for j in a if j>=0 and j<=9]
d=[k for k in a if k>=10 and k<=99]
t=[l for l in a if l>=100 and l<=999]
q=[m for m in a if m>=1000 and m<=9999]
print("single digit:",s)
print("double digit",d)
print("Triple digit:",t)
print("4-digit :",q)
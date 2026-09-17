# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 11:43:31 2026
sum of two matrices using list comprehension
@author: KAILASH L M
"""
a=[[int(input("Enter a value:"))for i in range(3)]for j in range(3)]
b=[[int(input("Enter a value:"))for k in range(3)]for l in range(3)]
print(a)
print(b)
s=[[a[x][y]+b[x][y] for y in range(3)]for x in range(3)]
print('SUM=',s)
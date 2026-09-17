# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 11:40:58 2026
conver into transpose matrices
@author: KAILASH L M
"""
a=[[int(input("Enter value:"))for i in range(3)]for j in range(3)]
b=[[a[c][r] for c in range(3)]for r in range(3)]
print(a)
print(b)
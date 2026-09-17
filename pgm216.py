# -*- coding: utf-8 -*-
"""
Created on Sat May 30 10:16:57 2026
Pascal triangle
@author: KAILASH L M
"""
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(' '*(n-i)+'*'*((2*i)-1))
    

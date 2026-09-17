# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:33:35 2026
*******
 *****
  ***
   *
   *
  ***
 *****
*******
@author: KAILASH L M
"""
n=int(input("Enter a number:"))
m=n
for i in range(n,0,-1):
    print(' '*(n-i)+'*'*((2*i)-1))
for j in range(1,m+1):
    print(' '*(m-j)+'*'*((2*j)-1))
    

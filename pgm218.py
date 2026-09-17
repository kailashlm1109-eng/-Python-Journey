# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:00:30 2026
    *
   ***
  *****
 *******
*********
*********
 *******
  *****
   ***
    *
@author: KAILASH L M
"""
n=int(input("Enter a number:"))
m=int(input("Enter a number:"))
for j in range(1,m+1):
    print(' '*(m-j)+'*'*((2*j)-1))
for i in range(n,0,-1):
    print(' '*(n-i)+'*'*((2*i)-1))


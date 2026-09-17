# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 10:54:15 2026
     *
    * *
   *   *
  *     *
   *   *
    * *
     *
@author: KAILASH L M
"""
n=int(input("Enter a number:"))
print(' '*(n-1)+'*')
for i in range(2,n):
    print(' '*(n-i)+'*'+' '*((2*i)-2)+'*')
for j in range(n-1,0,-1):
    print(' '*(n-j)+'*'+' '*((2*j)-1)+'*')
print(' '*(n)+'*')


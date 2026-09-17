# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:42:07 2026
*******
 *   *
  * *
   *
@author: KAILASH L M
"""
n=int(input("Enter a number:"))
print('*'*(2*n))
for i in range(n-1,0,-1):
    print(' '*(n-i)+'*'+' '*((2*i)-1)+'*')
print(' '*(n)+'*')

    
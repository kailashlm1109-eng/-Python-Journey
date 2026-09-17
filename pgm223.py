# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:35:34 2026
     *
    * *
   *   *
  *     *
 *********
@author: KAILASH L M
"""
n=int(input("Enter a number:"))
print(' '*(n-1)+'*')
for i in range(2,n):
    print(' '*(n-i)+'*'+' '*((2*i)-2)+'*')
print('*'*(2*n))

    


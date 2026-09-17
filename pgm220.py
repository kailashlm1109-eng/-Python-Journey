# -*- coding: utf-8 -*-
"""
Created on Sat May 30 11:36:41 2026
       1
      123
     12345
    1234567
     12345
      123
       1
@author: KAILASH L M
"""
n=int(input("Enter a number:"))
m=n-1
for i in range(1,n+1):
   print(' ' *(n-i),end='')
   for x in range(1,(2*i)):
        print(x,end='')
   print()
for j in range(m,0,-1):
    print(' '*(m-j),end=' ')
    for y in range(1,(2*j)):
        print(y,end='')
    print()
      
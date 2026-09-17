# -*- coding: utf-8 -*-
"""
Created on Sun May 31 11:27:18 2026
     a
    abc
   abcde
  abcdefg
   abcde
    abc
     a
@author: KAILASH L M
"""
n=int(input("Enter a number:"))
m=n-1
for i in range(1,n+1):
   print(' ' *(n-i),end='')
   for x in range(1,(2*i)):
        print(chr(x+96),end='')
   print()
for j in range(m,0,-1):
    print(' '*(m-j),end=' ')
    for y in range(1,(2*j)):
        print(chr(y+96),end='')
    print()
    


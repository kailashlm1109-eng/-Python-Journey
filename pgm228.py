# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 11:00:38 2026
     *
    *-*
   *-*-* 
  *-*-*-*
@author: KAILASH L M
"""
n=int(input("Enter a number:"))
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(1,2*i):
        if j%2==0:
            print('-',end='')
        else:
            print('*',end='')
    print()
        
    



# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 10:58:03 2026
*
*-*
*-*-
*-*-*
@author: KAILASH L M
"""
n=int(input("Enter number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2==0:
            print('-',end='')
        else:
            print('*',end='')
    print()



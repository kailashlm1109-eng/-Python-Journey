# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 10:24:59 2026

@author: KAILASH L M
"""
c=1
while c<=4:
    a=3
    b=1
    x=1
    while x<=a:
        print(" ",end='')
        print(' ',end='')
        x=x+1
    y=1
    while y<=b:
        if y%2==0:
            print('-',end='')
        else:
            print('*',end='')
        y=y+1
    c=c+1
    a=a-1
    b=b+2

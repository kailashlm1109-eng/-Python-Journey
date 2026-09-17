# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 10:17:10 2026
Pascal triangle      *
                    ***
                   *****
                  *******
@author: KAILASH L M
"""
a=3
b=1
c=1
while c<=4:
    n=1
    while n<=a:
        print(' ',end='')
        n=n+1
    x=1
    while x<=b:
        print('*',end="")
        x=x+1
    c=c+1
    a=a-1
    b=b+2
    print()
    

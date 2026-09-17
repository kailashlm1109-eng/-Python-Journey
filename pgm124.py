# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 10:37:44 2026
Multiplication table 1-12
@author: KAILASH L M
"""
c=1
while c<=12:
    n=1
    while n<=12:
        p=c*n
        print(n,"*",c,"=",p)
        n=n+1
    c=c+1
    print()

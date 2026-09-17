# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 10:21:31 2026

@author: KAILASH L M
"""
c=1
while c<=5:
    a=1
    while a<=c:
        if a%2==0:
            print('-',end='')
        else:
            print("*",end='')
        a=a+1
    c=c+1
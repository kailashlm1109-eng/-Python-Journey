# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 10:25:34 2026
pattern  ----*
         ---**
         --***
         -****
         *****
         -****
         --***
         ---**
         ----*
@author: KAILASH L M
"""
a=4
b=1
c=1
while c<=5:
    n=1
    while n<=a:
        print('-',end='')
        n=n+1
    x=1
    while x<=b:
        print('*',end='')
        x=x+1
    c=c+1
    a=a-1
    b=b+1
    print()
l=1
m=4
d=1
while d<=4:
    p=1
    while p<=l:
        print('-',end='')
        p=p+1
    q=1
    while q<=m:
        print('*',end='')
        q=q+1
    d=d+1
    l=l+1
    m=m-1
    print()
        

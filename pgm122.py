# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 10:33:13 2026
Fibonacci series
@author: KAILASH L M
"""
s=0
f=1
n=0
c=1
print("FIBONACCI SERIES")
while c<=10:
    n=s+f
    s=f
    f=n
    c=c+1
    print(s)

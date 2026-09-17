# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 10:08:35 2026
Read number from a keyboard & stroe it to a set
@author: KAILASH L M
"""
n=int(input("Enter a no. element in a set:"))
a=set()
for i in range(n):
    x=int(input("Enter an element:"))
    a.add(x)
print(a)

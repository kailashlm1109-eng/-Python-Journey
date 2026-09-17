# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:06:25 2026
find out the second biggest of set
@author: KAILASH L M
"""
s1={70,43,97,77,13,100,44,17,1,37}
print(s1)
a=max(s1)
print("Biggest:",a)
b=-101
for i in s1:
    b=i if b<i and i!=a else b
print("Second biggest:",b)
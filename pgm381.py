# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:26:46 2026
Find union, intersection, difference and symmetric difference of two sets
@author: KAILASH L M
"""
a={1,2,3,4,5,6,7,8,9,10}
b={2,4,6,8,10,12,14,16,18,20}
print(a)
print(b)
print("Union:",a.union(b))
print("Intersection:",a.intersection(b))
print("Difference:",a-b)
print("Symmetric_Difference",a^b)

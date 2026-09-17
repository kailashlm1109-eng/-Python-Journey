# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:50:02 2026
print dictionary 1 by 1
@author: KAILASH L M
"""
d={}
for i in range(3):
    name=input("Enter student name:")
    mark=[int(input("enter mark:"))for j in range(5)]
    d[name]=mark
print(d)

for k in d:
    print(k,d[k])

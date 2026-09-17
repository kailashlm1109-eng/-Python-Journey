# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:53:09 2026
print keys,values,items of dictionary
@author: KAILASH L M
"""
d={}
for i in range(3):
    name=input("Enter student name:")
    mark=[int(input("enter mark:"))for j in range(5)]
    d[name]=mark
print(d)
print("Keys:",d.keys())
print("Values:",d.values())
print("Items:",d.items())

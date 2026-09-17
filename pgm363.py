# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:23:22 2026
store student name and mark
@author: KAILASH L M
"""
d={}
for i in range(5):
    name=input("Enter student name:")
    mark=[int(input("Enter mark in subject:")) for j in range(5)]
    d[name]=mark
print(d)

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 09:49:36 2026

@author: KAILASH L M
"""
d={}
for i in range(5):
    name=input("Enter student name:")
    mark=[int(input("Enter mark in subject:")) for j in range(5)]
    d[name]=mark
print(d)


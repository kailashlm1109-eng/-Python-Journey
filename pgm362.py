# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 11:17:46 2026
store a list of cities into the dictionary by getting input
@author: KAILASH L M
"""
d={}
for i in range(3):
    st=input("Enter a state:")
    ci=[input("Enter cities in "+st+":") for j in range(3)]
    d[st]=ci
print(d)

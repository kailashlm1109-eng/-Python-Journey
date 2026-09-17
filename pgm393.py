# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 09:52:18 2026
Extract the common keywords of the given two text
@author: KAILASH L M
"""
s1=input("Enter a string:")
l1=s1.split()
a=set(l1)
s2=input("Enter a string:")
l2=s2.split()
b=set(l2)
c={'is','was','a','an','the','for','of','and','were','in'}
x=(a&b)-c
print(a)
print(b)
print(x)

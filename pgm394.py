# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 10:04:37 2026

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
p=(len(x)/(len(a)+len(b)))*100
print("The Percentage of common keyword is",p,"%")

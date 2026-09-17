# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 09:56:48 2026
no. of leap year b/w two limits o year
@author: KAILASH L M
"""
c=0
i=int(input("Enter a starting year:"))
f=int(input("Enter a ending year:"))
while i<=f:
    if i%4==0:
        c=c+1
    i=i+1
print("The number of leap year b/w two limits are:",c)

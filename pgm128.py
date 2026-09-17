# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 09:54:42 2026
no. of even b/w two limits
@author: KAILASH L M
"""
c=0
i=int(input("Enter a starting limit:"))
f=int(input("Enter a ending limit:"))
while i<=f:
    if i%2==0:
        c=c+1
    i=i+1
print("The number of even number b/w two limits are:",c)
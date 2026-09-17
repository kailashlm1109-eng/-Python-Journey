# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:09:31 2026
Frequency count of the text
@author: KAILASH L M
"""
s=input("Enter a String:")
l=s.split()
print(l)
x=set(l)
u=list(x)
print(u)
for i in u:
    print("Count of",i,"-",l.count(i))
    

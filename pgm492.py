# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 09:56:01 2026

@author: KAILASH L M
"""
import pickle
f=open("file",'rb')
l=pickle.load(f)
print(l)

s=[i for i in l if i>=0 and i<=9]
d=[j for j in l if j>=10 and j<=99]
t=[k for k in l if k>=100 and k<=999]
q=[m for m in l if m>=1000 and m<=9999]

print("Single digit:")
print(s)
print("Double digit:")
print(d)
print("Triple digit:")
print(t)
print("Quadouble digit:")
print(q)

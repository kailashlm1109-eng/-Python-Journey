# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:10:36 2026
second biggest
@author: KAILASH L M
"""
import random
n=int(input("Enter a number of value in a list:"))
a=[]
i=1
while i<=n:
    x=random.randint(-100,100)
    a.append(x)
    i=i+1
print(a)
b=-100
j=0
while j<n:
    if a[j]>b:
        b=a[j]
    else:
        pass
    j=j+1
s=-100
k=0
while k<n:
    if a[k]!=b:
        if a[k]>s:
            s=a[k]
        else:
            pass
    k=k+1
print("Second biggest:",s)




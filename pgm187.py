# -*- coding: utf-8 -*-
"""
Created on Sat May 16 11:25:08 2026
interchange second big and small
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
s=100
j=0
while j<n:
    if a[j]>b:
        b=a[j]
        y=j
    elif a[j]<s:
        s=a[j]
        z=j
    else:
        pass
    j=j+1
p=-100
q=100
k=0
while k<n:
    if a[k]!=b:
        if a[k]>p:
            p=a[k]
            l=k
    else:
        pass
    if a[k]!=s:
        if a[k]<q:
            q=a[k]
            m=k
        else:
            pass
    else:
        pass
    k=k+1
a[l]=q
a[m]=p
print(a)
            
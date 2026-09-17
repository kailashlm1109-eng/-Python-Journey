# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 10:18:41 2026
insert element before the smallest and after the biggest element
@author: KAILASH L M
"""
import random
l=[]
n=int(input("Enter a no. of elements in a list:"))
for j in range(n):
    x=random.randint(-10,10)
    l.append(x)
print("list:",l)
b=max(l)
p=l.index(b)
s=min(l)
q=l.index(s)
k=int(input("Enter a value insert after the Biggest element:"))
j=int(input("Enter a value insert after the Smallest element:"))
l.insert(p+1,k)
l.insert(q,j)
print(l)


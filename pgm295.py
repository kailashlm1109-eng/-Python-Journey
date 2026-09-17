# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 10:29:58 2026
sum,min,max,index of list
@author: KAILASH L M
"""
import random
a=[]
n=int(input("Enter a no. of elements in a list:"))
for j in range(n):
    x=random.randint(-100,100)
    a.append(x)
print(a)
print("Sum of list:",sum(a))
print("Biggest of list:",max(a))
print("Smallest of list:",min(a))
j=int(input("Enter a element in a list:"))
print("The index of the given element is :",a.index(j))

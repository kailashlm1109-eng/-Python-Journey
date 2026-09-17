# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 10:06:22 2026
count the positive negative and zero
@author: KAILASH L M
"""
import random
def rand_list():
    n=int(input("Enter no. of element :"))
    l=[random.randint(-100,100) for i in range(n)]
    return l
def count_list(x):
    global p,n,z
    p=0
    n=0
    z=0
    for j in x:
        if j>0:
            p+=1
        elif j<0:
            n+=1
        else:
            z+=1
#main
l1=rand_list()
print(l1)
count_list(l1)
print("Positive:",p)
print("Negative:",n)
print("Zero:",z)

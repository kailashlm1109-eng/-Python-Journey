# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:20:02 2026
Interchange Second Biggest and Second Smallest
@author: KAILASH L M
"""
import random
def rand_list():
    n=int(input("Enter no. of element in a list:"))
    l=[random.randint(-100,100) for i in range(n)]
    return l
def interchange_2bs(x):
    sb=-101
    ss=101
    for j in x:
        sb=j if sb<j and j!=max(x) else sb
        ss=j if ss>j and j!=min(x) else ss
    isb=x.index(sb)
    iss=x.index(ss)
    x[isb]=ss
    x[iss]=sb
def show_list(y):
    for l in y:
        print(l)
#main
l1=rand_list()
print(l1)
interchange_2bs(l1)
print(l1)
show_list(l1)

l2=rand_list()
print(l2)
interchange_2bs(l2)
print(l2)
show_list(l2)
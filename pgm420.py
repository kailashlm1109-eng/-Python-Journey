# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:13:58 2026
Interchange the Biggest and Smallest element(Function)
@author: KAILASH L M
"""
import random
def rand_list():
    n=int(input("Enter no. of element in a list:"))
    l=[random.randint(-100,100) for i in range(n)]
    return l

def interchange(x):
    b=max(x)
    s=min(x)
    bi=x.index(b)
    si=x.index(s)
    x[bi]=s
    x[si]=b
def show(y):
    for i in y:
        print(y)
#main
l1=rand_list()
print(l1)
interchange(l1)
print(l1)

l2=rand_list()
print(l2)
interchange(l2)
print(l2)
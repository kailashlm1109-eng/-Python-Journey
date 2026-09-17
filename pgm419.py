# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:09:22 2026
construct n random list and fin biggest smallest and index of biggest and smallest
@author: KAILASH L M
"""
import random
def random_list():
    n=int(input("Enter no. of element in a list:"))
    l=[random.randint(-100,100) for i in range(n)]
    return l
def bigsmall(x):
    b=max(x)
    s=min(x)
    print("Biggest:",b)
    print("Smallest:",s)
    print("Index of Biggest:",x.index(b))
    print("Index of Smallest:",x.index(s))
#main
l1=random_list()
print(l1)
bigsmall(l1)

l2=random_list()
print(l2)
bigsmall(l2)

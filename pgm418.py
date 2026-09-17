# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:05:43 2026
construct a list and print it in another func
@author: KAILASH L M
"""
import random
def random_list():
    n=int(input("Enter no. of element in a list:"))
    l=[random.randint(-100,100) for i in range(n)]
    return l
def show_list(x):
    for j in x:
        print(j)
#main
l1=random_list()
print(l1)
show_list(l1)

l2=random_list()
print(l2)
show_list(l2)
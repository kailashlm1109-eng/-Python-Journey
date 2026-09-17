# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 10:00:04 2026
count poitive negative and zero
@author: KAILASH L M
"""
import random
def rand_list():
    n=int(input("Entetr no. of element :"))
    l=[random.randint(-100,100) for i in range(n)]
    return l
def count_list(x):
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
    print("Positive25 count:",p)
    print("Negative count:",n)
    print("Zero count:",z)
#main
l1=rand_list()
print(l1)
count_list(l1)

l2=rand_list()
print(l2)
count_list(l2)

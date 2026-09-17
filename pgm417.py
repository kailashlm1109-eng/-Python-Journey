# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:02:55 2026
construct a list on n random number and print it in main
@author: KAILASH L M
"""
import random
def random_list():
    n=int(input("Enter no. of element in a list:"))
    l=[random.randint(-100,100) for i in range(n)]
    return l
#main
l1=random_list()
print(l1)
l2=random_list()
print(l2)

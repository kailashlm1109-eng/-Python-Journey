# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 10:39:53 2026
construct a list of n random numbers & Extract even numbers (Lambda)
@author: KAILASH L M
"""
import random
rand_list=lambda n:[random.randint(-100,100) for i in range(n)]
even_list=lambda l:[j for j in l if not j%2]

l1=rand_list(50)
e1=even_list(l1)
print(l1)
print("Even List:",e1)

l2=rand_list(50)
e2=even_list(l2)
print(l2)
print("Even List:",e2)
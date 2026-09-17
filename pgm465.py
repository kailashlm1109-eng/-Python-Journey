# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 10:37:55 2026
list of n random numbers (lambda function)
@author: KAILASH L M
"""
import random
rand_list=lambda n:[random.randint(-100,100) for i in range(n)]
#main
l1=rand_list(50)
print(l1)
l2=rand_list(100)
print(l2)
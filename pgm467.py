# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 10:43:56 2026
Extract only the 1-digit, 2-digit, 3-digit, 4-digit (lambda)
@author: KAILASH L M
"""
import random
rand_list=lambda n:[random.randint(-1000,10000) for i in range(n)]
s_digit=lambda l:[s for s in l if s>=0 and s<=9]
d_digit=lambda l:[s for s in l if s>=10 and s<=99]
t_digit=lambda l:[s for s in l if s>=100 and s<=999]
q_digit=lambda l:[s for s in l if s>=1000 and s<=9999]
#main
l1=rand_list(75)
s1=s_digit(l1)
d1=d_digit(l1)
t1=t_digit(l1)
q1=q_digit(l1)
print(l1)
print(d1)
print(t1)
print(q1)
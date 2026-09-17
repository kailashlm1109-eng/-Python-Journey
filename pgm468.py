# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 10:51:56 2026
Construct a 3 by 3 matrices
@author: KAILASH L M
"""
import random
matric=lambda :[[random.randint(-100,100) for i in range(3)]for j in range(3)]
m1=matric()
print(m1)
m2=matric()
print(m2)

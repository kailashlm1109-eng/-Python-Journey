# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 10:16:13 2026
call function by pass func by func
@author: KAILASH L M
"""
import math
def func(f):
    i=int(input("Enter a number:"))
    a=f(i)
    return a
#main
x=func(math.sin)
print(x)
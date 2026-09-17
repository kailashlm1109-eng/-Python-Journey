# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:46:50 2026
Sum of element of odd numbers using yield
@author: KAILASH L M
"""
def sum_odd(x):
    for i in range(x):
        if i%2:
            yield i
#main
s=0
for j in sum_odd(50):
    s+=j
print("Sum of odd numbers(1-50):",s)
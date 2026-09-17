# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:16:58 2026
construct a set using set comprehension
@author: KAILASH L M
"""
n=int(input("Enter a no. of element in a set:"))
a={int(input("Enter a element:")) for i in range(n)}
print(a)
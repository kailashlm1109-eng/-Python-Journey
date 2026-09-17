# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:21:52 2026
Smallest of 3 numbers (lambda)
@author: KAILASH L M
"""
small3=lambda a,b,c: a if a<c else c if a<b else b if b<c else c
s1=small3(20,17,47)
print("Smallest 1:",s1)
s2=small3(47,65,91)
print("Smallest 2:",s2)

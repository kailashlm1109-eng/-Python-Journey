# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:18:15 2026
Biggest of 3 (lambda)
@author: KAILASH L M
"""
big3=lambda a,b,c: a if a>c else c if a>b else b if b>c else c
b1=big3(68,53,48)
print("Biggest 1:",b1)
b2=big3(47,64,34)
print("Biggest 2:",b2)
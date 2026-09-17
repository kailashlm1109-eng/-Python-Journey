# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 11:22:40 2026
Find out the big small sum and indexes
@author: KAILASH L M
"""
def func(*x):
    b=max(x)
    s=min(x)
    a=sum(x)
    bi=x.index(b)
    si=x.index(s)
    print("Sum:",a)
    print("Biggest:",b)
    print("Index of Biggest:",bi)
    print("Smallest:",s)
    print("Index of Smallest:",si)
#main
func(77,57,68,74,2,55,477,55,77,557,44,52,4)
func(784,46,4,7,41,58,12,22,78,25,100,85,7)
func(45,75,12,77,6)
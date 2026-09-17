# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:40:55 2026
Sum of element in of odd index using yield
@author: KAILASH L M
"""
def sum_oddind(l):
    for i in l:
        if l.index(i)%2:
            yield i

#main
l1=[1,2,3,4,5,56,84,6,7,65,6,6,68,86,87,35,98,76,86,7,97,]
s=0
for j in sum_oddind(l1):
    s+=j
print("Sum of element in odd index of list:",s)
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 11:49:34 2026
sum of element of the list using yield function
@author: KAILASH L M
"""
def sum_list(l):
    for i in l:
        yield i
#main
l1=[54,4,87,5,21,7,5,4,7,997,66,46,466,46,87,7,35,24,68,42,7,64,4,97]
s=0
for j in sum_list(l1):
    s+=j
print("Sum of the list:",s)
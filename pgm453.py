# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:48:51 2026
Print only the even numbers (yield )Generators
@author: KAILASH L M
"""
def even(x):
    for i in range(x):
        if not i%2:
            yield i
#main
for i in even(10):
    print(i)
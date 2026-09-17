# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:26:28 2026
Biggest of three numbers(decorators)
@author: KAILASH L M
"""
def big2(a,b):
    b2=a if a>b else b
    return b2
def calculate(f,x,y,z):
    def big3():
        b2=f(x,y)
        b3=b2 if b2>z else z
        return b3
    return big3 

#main
s=calculate(big2,85,71,63)
p=s()
print("Biggest:",p)


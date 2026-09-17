# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:37:01 2026
Biggest of three by pass data in outer fun
@author: KAILASH L M
"""
def calculate(a,b,c):
    def big():
        return a if a>b and a>c else b if b>c else c
    x=big()
    return x
#main
b1=calculate(86,7,65)
print("Biggest 1:",b1)
b2=calculate(87,4,97)
print("Biggest 2:",b2)
b3=calculate(68,65,6)
print("Biggest 3:",b3)
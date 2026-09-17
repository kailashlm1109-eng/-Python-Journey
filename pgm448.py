# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 11:47:53 2026
Biggest of three numbers by getting function from inner function
@author: KAILASH L M
"""
def calculate(a,b,c):
    def big():
        m=a if a>b and a>c else b if b>c else c
        return m
    return big
#main
biggest=calculate(25,5,76)
x=biggest()
print("Biggest:",x)
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 10:15:41 2026
Sum of three interger (1 data in outer fn, 2 data in inner fn)
@author: KAILASH L M
"""
def s2(a,b):
    return a+b
def calculate(f,x,y,z):
    def s3():
        s=f(x,y)+z   #Decorators
        return s
    return s3 
#main
s=calculate(s2, 10, 20, 30)
x=s()
print("Sum:",x)

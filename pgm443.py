# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 11:27:13 2026
sum of two numbers by passing data in outer
@author: KAILASH L M
"""
def calculate(a,b):
    def add():
        return a+b
    x=add()
    return x
#main
s1=calculate(65,7)
print("SUM 1:",s1)
s2=calculate(89,46)
print("SUM 2:",s2)
s3=calculate(79,97)
print("SUM 3:",s3)


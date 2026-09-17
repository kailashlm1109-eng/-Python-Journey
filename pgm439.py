# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 10:30:59 2026
retrun big func by return to another func
@author: KAILASH L M
"""
def big(x,y,z):
    b=x if x>y and x>z else y if y>z else z
    return b
def calculate():
    return big
#main
max_num=calculate()
b1=max_num(5,1,7)
print("BIG:",b1)
b2=max_num(65,44,77)
print("Big:",b2)
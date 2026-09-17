# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 10:35:22 2026
Sum of two integer numbers (default arguments)
@author: KAILASH L M
"""
def sum(a=5,b=10):
    s=a+b
    return s
#main
s1=sum()
s2=sum(20)
s3=sum(15,20)
s4=sum(b=50)
print("Sum 1:",s1)
print("Sum 2:",s2)
print("Sum 3:",s3)
print("Sum 4:",s4)

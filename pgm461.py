# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 11:09:19 2026
Find out the sum diff prod and quoti of given two numbers in single lambda fn
@author: KAILASH L M
"""
calc=lambda a,b:(a+b,a-b, a*b, a/b)
s1,d1,p1,q1=calc(10,20)
print("Sum 1:",s1)
print("Difference 2:",d1)
print("Product 1:",p1)
print("Quotient 1:",q1)
s2,d2,p2,q2=calc(12.5,17.3)
print("Sum 2:",s2)
print("Difference 2:",d2)
print("Product 2:",p2)
print("Quotient 2:",q2)
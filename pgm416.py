# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 09:32:02 2026
pass bio data to function and print it in key value pair
@author: KAILASH L M
"""
def bio(**x):
    print(x)
    print(x.items())

#main
bio(Name='KAILASH',Age=18,DOB='11-04-2009',Gender='Male',Education='12th')
bio(Name='HARISH',Age=19,DOB='28-07-2008',Gender='Male',Education='10th')


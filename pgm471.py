# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 09:34:14 2026
Read number other than thousand
@author: KAILASH L M
"""
def other1000():
    a=int(input("Enter the number:"))
    return a
#main
i=other1000()
while i!=1000:
    print(i)
    i=other1000()
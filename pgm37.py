# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 11:47:11 2026
biggest of three digit number
@author: KAILASH L M
"""
n=int(input("Enter a 3-digit number:"))
a=n%10
x=n//10
b=x%10
c=x//10
if a>b:
    if a>c:
        print(a,"is BIGGEST")
    else:
        print(c,"is BIGGEST")
else:
    if b>c:
        print(b,"is BIGGEST")
    else:
        print(c,"is BIGGEST")

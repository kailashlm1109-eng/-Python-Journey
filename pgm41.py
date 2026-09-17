# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:42:55 2026
1-digit/2-digit/3-digit
@author: KAILASH L M
"""
a=int(input("Enter a number:"))
if a>=0 and a<=9:
    print(a,"is single digit")
elif a>10 and a<=99:
    print(a,"is a 2-digit number")
elif a>100 and a<=999:
    print(a,"is three digit number")
else:
    print(a,"is more than 3-digit number")
    
    
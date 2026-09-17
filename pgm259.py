# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:15:37 2026
flip the alphabets
@author: KAILASH L M
"""
s=input("Enter a string:")
s1=''
for i in s:
    n=ord(i)
    if n>=65 and n<=90:
        s1+=chr(n+32)
    elif n>=97 and n<-122:
        s1+=chr(n-32)
    else:
        s1+=i
print(s1)


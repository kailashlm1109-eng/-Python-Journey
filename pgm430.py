# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 11:12:13 2026
count upper, lower, digit, spl character
@author: KAILASH L M
"""
def count_string(s):
    global u,l,d,x
    u=0
    l=0
    d=0
    x=0
    for i in s:
        if i>='0' and i<='9':
            d+=1
        elif i>='a' and i<='z':
            l+=1
        elif i>='A' and i<='Z':
            u+=1
        else:
            x+=1
#main
s1=input("Enter a character:")
count_string(s1)
print("Upper:",u)
print("Lower:",l)
print("Digit:",d)
print("Spl Character:",x)

s2=input("Enter a character:")
count_string(s2)
print("Upper:",u)
print("Lower:",l)
print("Digit:",d)

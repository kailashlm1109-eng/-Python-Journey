# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 11:02:29 2026
count vowels and nonvowels of the given string
@author: KAILASH L M
"""
def count_string(s):
    global x,y
    x=0
    y=0
    for i in s:
        if i in 'AEIOU':
            x+=1
        else:
            y+=1
#main
s1=input("Enter a characters:")
count_string(s1)
print("Count of Vowels:",x)
print("Count of Non Vowels:",y)

s2=input("Enter a characters:")
count_string(s2)
print("Count of Vowels:",x)
print("Count of Non Vowels:",y)


    
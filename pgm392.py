# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 11:57:03 2026
print the unique word of the text by remove stopwords
@author: KAILASH L M
"""
s=input("Enter a string:")
l=s.split()
a=set(l)
b={'is','was','a','an','the','were','of','if','are','were'}
print(a)
x=a-b
print(x)


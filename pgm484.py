# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 09:55:58 2026
Print Only the keyword
@author: KAILASH L M
"""
f1=open(r"C:\Apps\YR2T2\pytext.txt",'r')
f2=open(r"C:\Apps\YR2T2\stopwords.txt",'r')
x1=f1.read()
y1=x1.split()
a=set(y1)
print("UNIQUE WORDS:")
print(a)
x2=f2.read()
y2=x2.split()
b=set(y2)
print()
print("STOP WORDS:")
print(b)
k=a-b
print()
print("KEYWORDS:")
print(k)


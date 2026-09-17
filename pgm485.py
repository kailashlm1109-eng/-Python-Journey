# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:39:18 2026
display only the common keyword betwaeen the two text file
@author: KAILASH L M
"""
s=open(r"C:\Apps\YR2T2\stopwords.txt",'r')
t1=open(r"C:\Apps\YR2T2\pytext.txt",'r')
t2=open(r"C:\Apps\YR2T2\pytext1.txt",'r')
x1=t1.read()
y1=x1.split()
a=set(y1)

x2=t2.read()
y2=x2.split()
b=set(y2)

x3=s.read()
y3=x3.split()
s1=set(y3)


k1=a-s1
print()
print("File 1:")
print(k1)
k2=b-s1
print()
print("File 2:")
print(k2)
print()
print("Stop Words:")
print(s1)

i=k1&k2
print()
print("Common Words:")
print(i)
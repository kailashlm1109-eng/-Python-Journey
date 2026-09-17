# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:30:05 2026
Read the first five line of the text file
@author: KAILASH L M
"""
f=open(r"C:\Apps\YR2T2\pytext.txt",'r')
x1=f.readline()
x2=f.readline()
x3=f.readline()
x4=f.readline()
x5=f.readline()
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
f.close()
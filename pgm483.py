# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 09:42:52 2026
Print only the unique words of the file
@author: KAILASH L M
"""
f=open(r"C:\Apps\YR2T2\pytext.txt",'r')
x=f.read()
y=x.split()
u=set(y)
print(u)
f.close()
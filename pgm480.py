# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 10:34:00 2026
Store count of words and characters in dictionary
@author: KAILASH L M
"""
f=open(r"C:\Apps\YR2T2\pytext.txt",'r')
a=1
d={}
for r in f:
    x=r.split()
    cw=len(x)
    cl=len(r)
    d[a]=cw,cl
    a+=1
print(d)
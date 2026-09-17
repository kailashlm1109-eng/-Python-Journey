# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 11:04:18 2026
longest line of the text file in dictionary
@author: KAILASH L M
"""
f=open(r"C:\Apps\YR2T2\pytext.txt",'r')
a=1
d={}
for r in f:
    cl=len(r)
    x=r.split()
    cw=len(x)
    d[a]=cl,cw
    a+=1
print(d)
v=d.values()
m=max(v)
for i in range(1,a):
    if d[i]==m:
        print(i,"is the longest line")
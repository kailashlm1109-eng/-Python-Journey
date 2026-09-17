# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 10:16:12 2026
No. of words & No. of letters in each line
@author: KAILASH L M
"""
f=open(r"C:\Apps\YR2T2\pytext.txt",'r')
a=1
for r in f:
    print(r)
    x=r.split()
    cw=len(x)
    cl=len(r)
    print(f"No. of words in line {a}: {cw}")
    print(f"No. of letters in line {a}: {cl}")
    a+=1
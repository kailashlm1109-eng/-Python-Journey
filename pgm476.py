# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 10:47:36 2026
display text file line by line file as iterable object
@author: KAILASH L M
"""
f=open(r"C:\Apps\YR2T2\pytext.txt",'r')
for r in f:
    print(r)
f.close()
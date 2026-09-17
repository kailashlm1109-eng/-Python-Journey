# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 11:58:23 2026
display page by page
@author: KAILASH L M
"""
f=open(r"C:\Apps\YR2T2\pytext.txt",'r')
x=1
y=5
for r in f:
    if not x%y:
        print(x,". ",r)
        y=int(input("Enter number of line:"))
        x=1
    else:
        print(x,". ",r)
        x+=1
f.close()
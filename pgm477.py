# -*- coding: utf-8 -*-KAILASH
"""
Created on Fri Jul 17 11:09:22 2026
Display the text along the line numbers
@author: KAILASH L M
"""
f=open(r"C:\Apps\YR2T2\pytext.txt",'r')
x=1
for r in f:
    if r!='':
        print(x,". ",r)
    x+=1
f.close()
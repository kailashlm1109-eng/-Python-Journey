# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:22:12 2026
construct a set of n random number and extract 1-digit, 2-dgit, 3-digit,4-digit
@author: KAILASH L M
"""
import random
n=int(input("Enter a no. of element in a set:"))
a={random.randint(0,10000) for i in range(n)}
s={i for i in a if i>=0 and i<=9}
d={j for j in a if j>=10 and j<=99}
t={k for k in a if k>=100 and k<=999}
q={l for l in a if l>=1000 and l<=9999}
print(a)
print("Single digit:",s)
print("Double digit:",d)
print("Triple digit",t)
print("Foru digit",q)
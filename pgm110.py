# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 12:10:42 2026
   a
  abc
 abcde
abcdefg
 abcde
  abc
   a
@author: KAILASH L M
"""
a=3
b=1
c=1
while c<=4:
    n=1
    while n<=a:
        print(' ',end='')
        n=n+1
    x=1
    while x<=b:
        k= chr(x+96)
        print(k,end="")
        x=x+1
    c=c+1
    a=a-1
    b=b+2
    print()
p=1
q=5
d=1
while d<=3:
    y=1
    while y<=p:
        print(' ',end='')
        y=y+1
    z=1
    while z<=q:
        t= chr(z+96)
        print(t,end="")
        z=z+1
    d=d+1
    p=p+1
    q=q-2
    print()


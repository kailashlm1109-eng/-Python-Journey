# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 11:07:21 2026
plagerism of the text files
@author: KAILASH L M
"""
t=open(r"C:\Apps\YR2T2\pytext.txt",'r')
s=open(r"C:\Apps\YR2T2\stopwords.txt",'r')
x=t.read()
y=x.split()
f=set(y)

x1=s.read()
y1=x1.split()
st=set(y1)

k=f-st
print("FILE:")
print(k)
print()

for i in range(4):
    n=input("Enter File name:")
    f=open(n,'r')
    r1=f.read()
    x2=r1.split()
    f1=set(x2)
    k1=f1-st
    print("Given File:")
    print(k1)
    cn=k1&k
    p=(len(cn)/len(k1))*100
    print()
    print("Percentage of plagerism:", p,'%')
    print()
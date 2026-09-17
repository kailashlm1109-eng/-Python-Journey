# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 10:14:14 2026
Store all file ina a file
@author: KAILASH L M
"""
t=open(r"C:\Apps\YR2T2\pytext.txt",'r')
s=open(r"C:\Apps\YR2T2\stopwords.txt",'r')

r1=s.read()
x1=r1.split()
s1=set(x1)

r2=t.read()
x2=r2.split()
f1=set(x2)

k=f1-s1

print("ORIGINAL FILE")
print()
print(k)

t1=open("C:/Apps/YR2T2/FILES.txt",'r')
r=t1.read()
x=r.split()
print()
print("S.no"," ","No. of Line"," ","No. of Word"," ","Common Word","     ","Plagiarism")
a=1
for i in x:
    f=open(i,'r')
    r3=f.read()
    x3=r3.split()
    f2=set(x3)
    
    k1=f2-s1
    cn=k&k1
    p=(len(cn)/len(k1))*100
    print()
    print(" ",a,"       ",len(k1),"       ",len(r3),"         ",len(cn),"         ",p,"%")
    a+=1

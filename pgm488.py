# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:07:24 2026
Plagiarism by store text file in a list
@author: KAILASH L M
"""
t=open(r"C:\Apps\YR2T2\pytext.txt",'r')
s=open(r"C:\Apps\YR2T2\stopwords.txt",'r')
l=[r"C:\Apps\YR2T2\pytext.txt",r"C:\Apps\YR2T2\pytext1.txt",r"C:\Apps\YR2T2\pytext2.txt",r"C:\Apps\YR2T2\pytext3.txt",r"C:\Apps\YR2T2\pytext4.txt",]

r=s.read()
x=r.split()
s1=set(x)

r1=t.read()
x1=r1.split()
f=set(x1)

k=f-s1
print("ORIGINAL FILE:")
print("Number of line:",len(k))
print("Number of Keyword:",len(r1))
print()
a=1
print("S.no"," ","No. of Line"," ","No. of Word"," ","Common Word","     ","Plagiarism")
print()
for i in l:
    t1=open(i,'r')
    r2=t1.read()
    f1=r2.split()
    x2=set(f1)
    k1=x2-s1
    cn=k1&k
    p=(len(cn)/len(k1))*100
    print(" ",a,"       ",len(k1),"       ",len(r2),"        ",len(cn),"       ",p,"%")
    print()
    a+=1
    t1.close()
s.close()
t.close()
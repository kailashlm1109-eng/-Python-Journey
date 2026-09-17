# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:00:48 2026
store single digit double digit triple digit and quadouble digit into seperate file
@author: KAILASH L M
"""
import pickle
f=open("file",'rb')
l=pickle.load(f)
print("Main File:")
print()
print(l)

s=[i for i in l if i>=0 and i<=9]
d=[j for j in l if j>=10 and j<=99]
t=[k for k in l if k>=100 and k<=999]
q=[m for m in l if m>=1000 and m<=9999]

single=open("s1",'wb')
double=open("d1",'wb')
triple=open("t1",'wb')
quadouble=open("q1",'wb')

pickle.dump(s,single)
pickle.dump(d,double)
pickle.dump(t,triple)
pickle.dump(q,quadouble)

single.close()
double.close()
triple.close()
quadouble.close()

s2=open("s1",'rb')
d2=open("d1",'rb')
t2=open("t1",'rb')
q2=open("q1",'rb')

sd=pickle.load(s2)
dd=pickle.load(d2)
td=pickle.load(t2)
qd=pickle.load(q2)

print("Single digit:")
print(sd)
print()
print("Double digit:")
print(dd)
print()
print("Triple digit:")
print(td)
print()
print("Quadouble digit:")
print(qd)

f.close()
s2.close()
d2.close()
t2.close()
q2.close()
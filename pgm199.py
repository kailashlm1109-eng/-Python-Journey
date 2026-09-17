# -*- coding: utf-8 -*-
"""
Created on Thu May 21 11:03:59 2026
print person 1by1
@author: KAILASH L M
"""
n=int(input("Enter number of persons:"))
a=[]
i=1
l=[]
while i<=n:
    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    dob=input("Enter your Date Of Birth:")
    gender=input("Enter your Gender:")
    edu=input("Enter your Educational Qualification:")
    l=[name,age,dob,gender,edu]
    a.append(l)
    i=i+1
print(l)
j=0
while j<n:
    print(a[j])
    j=j+1


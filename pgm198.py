# -*- coding: utf-8 -*-
"""
Created on Thu May 21 10:54:29 2026
more than 1 bio data
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
print(a)




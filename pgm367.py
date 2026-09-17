# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 10:53:34 2026
print value by value of multiple bio data dictionary
@author: KAILASH L M
"""
d={}
for i in range(3):
    name=input("Enter name:")
    age=int(input("Enter age:"))
    dob=input("Enter Date of Birth:")
    edu=input("Enter your Education Qualification:")
    gender=input("Enter Gender:")
    d['student',i+1]=[name,age,dob,edu,gender]
print(d)
for j in d:
    for k in d[j]:
        print(k,end='  ')
    print()

# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 11:37:53 2026
Remove a key value pair from a dictionary
@author: KAILASH L M
"""
d={}
for i in range(3):
    key=input("Enter a key:")
    name=input("Enter name:")
    age=int(input("Enter age:"))
    dob=input("Enter Date of Birth:")
    edu=input("Enter your Education Qualification:")
    gender=input("Enter Gender:")
    d[key]=[name,age,dob,edu,gender]
print(d)
a=input("Enter key to delete:")
del d[a]
print(d)
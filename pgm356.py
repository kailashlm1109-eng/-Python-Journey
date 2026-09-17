# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:12:07 2026
construct a bio data dictionary by getting input
@author: KAILASH L M
"""
d={}
name=input("Enter your name:")
age=int(input("Enter age:"))
dob=input("Enter your Date of Birth:")
gender=input("Enter your gender:")
edu=input("Enter your Education qualification:")
d['name']=name
d['age']=age
d['dob']=dob
d['gender']=gender
d['class']=edu
print(d)
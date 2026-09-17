# -*- coding: utf-8 -*-
"""
Created on Mon Jun 15 10:16:55 2026
construct a dictionary of bio data by getting input
@author: KAILASH L M
"""
name=input("Enter your name:")
age=int(input("Enter your age:"))
dob=input("Enter your Date of Birth:")
gender=input("Enter your Gender:")
edu=input("Enter your Education qualification:")
d=dict(NAME=name,AGE=age,DOB=dob,GENDER=gender,CLASS=edu)
print(d)

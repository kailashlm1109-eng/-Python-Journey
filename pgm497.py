# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:18:49 2026
print data by data
@author: KAILASH L M
"""
import csv
f=open("D:/Python/python.csv",'r')
l=csv.reader(f)

for i in l:
    print("Roll No:",i[0])
    print("Name:   ",i[1])
    print("Age:    ",i[2])
    print("Tamil:  ",i[3])
    print("English:",i[4])
    print("Maths:  ",i[5])
    print("Science:",i[6])
    print("Social Science:",i[7])
    print()

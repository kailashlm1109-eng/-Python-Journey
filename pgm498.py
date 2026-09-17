# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 09:48:39 2026
print like marksheet
@author: KAILASH L M
"""
import csv
f=open("D:/Python/python.csv",'r')
l=csv.reader(f)

for i in l:
    s=0
    for j in range(3,8):
        s+=int(i[j])
        if int(i[j])>=35:
            a="PASS"
        else:
            a="FAIL"
            break
    
    print("         CLASS XII MARKSHEET")
    print("          ABC PUBLIC SCHOOL")
    
    print("Roll No:",i[0])
    print("Name:   ",i[1])
    print("Age:    ",i[2])
    print("Tamil:  ",i[3])
    print("English:",i[4])
    print("Maths:  ",i[5])
    print("Science:",i[6])
    print("Social Science:",i[7])
    print("Total:",s,"/500")
    print(a)
    print()

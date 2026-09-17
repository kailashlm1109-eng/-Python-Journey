# -*- coding: utf-8 -*-
"""
Created on Fri Jul 31 10:45:42 2026
print student marksheet
@author: KAILASH L M
"""
import csv
f=open("D:/Python/python.csv",'r')
l=csv.reader(f)

s=["Roll No:","Name:   ","Age:    ","Tamil:  ","English:","Maths:  ","Science:","Social Science:"]
for i in l:
    print("         CLASS XII MARKSHEET")
    print("          ABC PUBLIC SCHOOL")
    sm=0
    for j in range(8):
        if j>=3:
            sm+=int(i[j])
            if int(i[j])>=35:
                a="PASS"
            else:
                a="FAIL"
            print(s[j],i[j],"(",a,")")
        else:
            print(s[j],i[j])
    print("Total:",sm,"/500")
    print()
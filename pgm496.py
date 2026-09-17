# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:11:39 2026
print csv file line by line
@author: KAILASH L M
"""
import csv
f=open("D:/Python/python.csv",'r')
l=csv.reader(f)

for i in l:
    print(i)  
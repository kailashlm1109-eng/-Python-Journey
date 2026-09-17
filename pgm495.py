# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:04:31 2026
load entire csv file & print it
@author: KAILASH L M
"""
import csv
f=open("D:/Python/python.csv",'rb')
l=csv.reader(f)
print(l)
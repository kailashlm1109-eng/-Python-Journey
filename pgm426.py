# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 11:46:03 2026
construct a dictionary of n student and print in to another function
@author: KAILASH L M
"""
def dictionary():
    n=int(input("Enter no. of student in a dict:"))
    d={}
    for i in range(n):
        key=int(input("Enter Student's Roll:"))
        value=input("Enter student Name:")
        d[key]=value
    return d
def show_dict(x):
    print(x.items())

#main
d1=dictionary()
show_dict(d1)

d2=dictionary()
d2=show_dict(d2)
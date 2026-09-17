# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 17:12:34 2026
arithmatic/logical/relational/other
@author: KAILASH L M
"""

a=(input("Enter a operator:"))
if  a=='+' or a=='-' or a=='*' or a=='/' or a=='%' or a=='**' or a=='//':
    print(a,"is an Arithmatic operator")
elif a=='>' or a=='<' or a=='>=' or a=='<=' or a=='==':
    print(a,"is a Relational operator")
elif a=='and' or a=='or' or a=='not':
    print(a,"is a logical operator")
else:
    print(a,"is other operator")
    
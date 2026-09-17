# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:13:47 2026
arithmatic or not
@author: KAILASH L M
"""
a=input("Enter a Operator:")
match(a):
    case '+'|'-'|'*'|'/'|'%'|'//'|'**':
        print(a,"is Arithmatic operator")
    case _:
        print(a,"is not an Arithmatic operator")
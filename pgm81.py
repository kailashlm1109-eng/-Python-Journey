# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:19:59 2026
logic or not
@author: KAILASH L M
"""
a=input("Enter a Operator:")
match(a):
    case 'and'|'or'|'not':
        print(a,"is logical operator")
    case _:
        print(a,"is not an logical operator")

# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:17:11 2026
Relational or not
@author: KAILASH L M
"""
a=input("Enter a Operator:")
match(a):
    case '<'|'>'|'<='|'>='|'==':
        print(a,"is Relational operator")
    case _:
        print(a,"is not a Relational operator")

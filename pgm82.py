# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:21:23 2026
Arithmatic/logical/Relational/other
@author: KAILASH L M
"""
a=input("Enter a Operator:")
match(a):
    case '+'|'-'|'*'|'/'|'%'|'//'|'**':
        print(a,"is Arithmatic operator")
    case '<'|'>'|'<='|'>='|'==':
        print(a,"is Relational operator")
    case 'and'|'or'|'not':
        print(a,"is logical operator")
    case _:
        print(a,"is any other operator")

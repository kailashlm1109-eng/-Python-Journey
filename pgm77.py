# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:06:32 2026
vowel to word match
@author: KAILASH L M
"""
a=input("Enter a vowel:")
match(a):
    case 'A':
        print(a,"-APPLE")
    case 'E':
        print(a,"-ELEPHANT")
    case 'I':
        print(a,"-INK")
    case 'O':
        print(a,"-OWL")
    case 'U':
        print(a,"-UMBERLA")
    case _:
        print(a,"-not a vowel")

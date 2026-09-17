# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 11:07:06 2026
vowel to word
@author: KAILASH L M
"""
a=input("Enter a vowel:")
match(a):
    case 'A'|'a':
        print(a,"-APPLE")
    case 'E'|'e':
        print(a,"-ELEPHANT")
    case 'I'|'i':
        print(a,"-INK")
    case 'O'|'o':
        print(a,"-OWL")
    case 'U'|'u':
        print(a,"-UMBERLA")
    case _:
        print(a,"-not a vowel")
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 10:56:02 2026
Extract words ends with vowel
@author: KAILASH L M
"""
a=['KAILASH','ARYA','INIIYAN','VIJAY','HARI','SURIYA','SOORI']
print(a)
b=[i for i in a if i[-1] in "AEIOU"]
print(b)

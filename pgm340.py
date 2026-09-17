# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 10:53:54 2026
Extract the words start from vowel
@author: KAILASH L M
"""
a=['KAILASH','AJITH','INIYAN','VIJAY','ARAVIND']
print(a)
b=[i for i in a if i[0] in "AEIOU"]
print(b)

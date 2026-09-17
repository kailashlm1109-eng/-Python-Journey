# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 10:52:21 2026
extract only 4 letters words
@author: KAILASH L M
"""
a=['KAILASH','AJITH','RAVI','VIJAY','HARI','SIVA']
print(a)
b=[i for i in a if len(i)==4]
print(b)

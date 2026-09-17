# -*- coding: utf-8 -*-
"""
Created on Fri Jun 12 10:58:25 2026
Extract a words ends with ing
@author: KAILASH L M
"""
a=['READING','WRITE','LISTENING','PLAY','SLEEPING','TYPING','CLEANING','CLEAN']
print(a)
b=[i for i in a if i[-3:]=='ING']
print(b)


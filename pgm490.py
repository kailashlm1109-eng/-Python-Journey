# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:11:37 2026
store & dum; file
@author: KAILASH L M
"""
import random
import pickle
f=open("file",'wb')
n=int(input("Enter number of values:"))
a=[random.randint(0,100000) for i in range(n)]
pickle.dump(a,f)
f.close()
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 11:14:51 2026
load and display the binary file
@author: KAILASH L M
"""
import pickle
f1=open("file",'rb')
l=pickle.load(f1)
print(l)
f1.close()
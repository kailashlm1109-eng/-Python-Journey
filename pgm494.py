# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 10:22:49 2026
load a image and display it
@author: KAILASH L M
"""
import pickle
f=open("C:/Users/M.KIRUBHASHINI/Downloads/Lion.jpg",'rb')
s=pickle.load(f)
print(s)
f.close()
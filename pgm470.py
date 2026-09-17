# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 10:56:33 2026
sum of two matrices lambda
@author: KAILASH L M
"""
matric=lambda :[[int(input()) for i in range(3)]for j in range(3)]
sum_matric=lambda x,y:[[x[i][j]+y[i][j] for j in range(3)]for i in range(3)]
m1=matric()
print(m1)
m2=matric()
print(m2)
s=sum_matric(m1,m2)
print("SUM:",s)
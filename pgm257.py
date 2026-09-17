"""
Created on Thu Sep 17 21:06:26 2026
Convert text to lowercase
@author: KAILASH L M
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 10:13:44 2026
READ AND COVERT INTO LOWER
@author: KAILASH L M
"""
s=input("Enter a string:")
s1=''
for i in s:
    n=ord(i)
    if n>=65 and n<=90:
        s1+=chr(n+32)
    else:
        s1+=i
print(s1)

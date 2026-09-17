# -*- coding: utf-8 -*-
"""
Created on Thu May  7 11:09:49 2026
count of vowel and consonant
@author: KAILASH L M
"""
s=input("Enter a string:")
l=len(s)
i=0
v=0
c=0
while i<l:
    if s[i]=='A' or s[i]=='E' or s[i]=='I' or s[i]=='O' or s[i]=='U':
        v=v+1
    else:
        c=c+1
    i=i+1
print("VOWELS:",v)
print("CONSONANTS",c)

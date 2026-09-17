# -*- coding: utf-8 -*-
"""
Created on Sun May  3 10:45:23 2026
print only vowels in a string
@author: KAILASH L M
"""
text = input("Enter a string: ")
for character in text:
	if character.upper() in "AEIOU":
		print(character)


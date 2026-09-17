"""
Created on Thu Sep 17 21:06:26 2026
Count vowels and consonants
@author: KAILASH L M
"""
# Count vowels and consonants
text = input("Enter a string: ")
vowels = 0
consonants = 0
for character in text.lower():
    if character in "aeiou":
        vowels += 1
    elif character.isalpha():
        consonants += 1
print("Vowels:", vowels)
print("Consonants:", consonants)

"""
Created on Thu Sep 17 21:06:26 2026
Count digits, letters, and spaces
@author: KAILASH L M
"""
# Count digits, letters, and spaces
text = input("Enter a string: ")
digits = letters = spaces = 0
for character in text:
    if character.isdigit():
        digits += 1
    elif character.isalpha():
        letters += 1
    elif character.isspace():
        spaces += 1
print("Letters:", letters)
print("Digits:", digits)
print("Spaces:", spaces)

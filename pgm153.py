"""
Created on Thu Sep 17 21:06:26 2026
Replace vowels with a star
@author: KAILASH L M
"""
# Replace vowels with a star
text = input("Enter a string: ")
result = ""
for character in text:
    result += "*" if character.lower() in "aeiou" else character
print(result)

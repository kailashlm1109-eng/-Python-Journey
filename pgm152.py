"""
Created on Thu Sep 17 21:06:26 2026
Remove spaces from a string
@author: KAILASH L M
"""
# Remove spaces from a string
text = input("Enter a string: ")
result = ""
for character in text:
    if not character.isspace():
        result += character
print(result)

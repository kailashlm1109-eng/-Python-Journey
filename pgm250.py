"""
Created on Thu Sep 17 21:06:26 2026
Count each character in a string
@author: KAILASH L M
"""
# Count each character in a string
text = input("Enter a string: ")
counts = {}
for character in text:
    counts[character] = counts.get(character, 0) + 1
for character, count in counts.items():
    print(character, ":", count)

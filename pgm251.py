"""
Created on Thu Sep 17 21:06:26 2026
Find the most frequent character
@author: KAILASH L M
"""
# Find the most frequent character
text = input("Enter a string: ")
counts = {}
for character in text:
    counts[character] = counts.get(character, 0) + 1
if counts:
    character = max(counts, key=counts.get)
    print("Most frequent:", character)

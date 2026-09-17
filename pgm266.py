"""
Created on Thu Sep 17 21:06:26 2026
Find the longest word
@author: KAILASH L M
"""
# Find the longest word
words = input("Enter words separated by spaces: ").split()
if words:
    print("Longest word:", max(words, key=len))

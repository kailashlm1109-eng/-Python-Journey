"""
Created on Thu Sep 17 21:06:26 2026
Find the shortest word
@author: KAILASH L M
"""
# Find the shortest word
words = input("Enter words separated by spaces: ").split()
if words:
    print("Shortest word:", min(words, key=len))

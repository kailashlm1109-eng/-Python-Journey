"""
Created on Thu Sep 17 21:06:26 2026
Check whether two words are anagrams
@author: KAILASH L M
"""
# Check whether two words are anagrams
first = input("Enter the first word: ").replace(" ", "").lower()
second = input("Enter the second word: ").replace(" ", "").lower()
print("Anagrams" if sorted(first) == sorted(second) else "Not anagrams")

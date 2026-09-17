"""
Created on Thu Sep 17 21:06:26 2026
Find the first and last character
@author: KAILASH L M
"""
# Find the first and last character
text = input("Enter a non-empty string: ")
if text:
    print("First character:", text[0])
    print("Last character:", text[-1])
else:
    print("The string is empty")

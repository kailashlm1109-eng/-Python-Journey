"""
Created on Thu Sep 17 21:06:26 2026
Check whether a string is a palindrome
@author: KAILASH L M
"""
# Check whether a string is a palindrome
text = input("Enter a string: ")
cleaned = text.replace(" ", "").lower()
if cleaned == cleaned[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")

"""
Created on Thu Sep 17 21:06:26 2026
Check whether a number is a palindrome
@author: KAILASH L M
"""
# Check whether a number is a palindrome
number = input("Enter a number: ")
print("Palindrome" if number == number[::-1] else "Not a palindrome")

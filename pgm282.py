"""
Created on Thu Sep 17 21:06:26 2026
Find the union and intersection of two sets
@author: KAILASH L M
"""
# Find the union and intersection of two sets
first = set(input("Enter first set: ").split())
second = set(input("Enter second set: ").split())
print("Union:", first | second)
print("Intersection:", first & second)

"""
Created on Thu Sep 17 21:06:26 2026
Pattern: alternating star and dash triangle
*
*-
*-*
*-*-
*-*-*
@author: KAILASH L M
"""
# Pattern: alternating star and dash triangle
n = int(input("Enter number of rows: "))
for row in range(1, n + 1):
    for column in range(1, row + 1):
        print("*" if column % 2 else "-", end="")
    print()

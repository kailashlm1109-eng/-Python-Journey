"""
Created on Thu Sep 17 21:06:26 2026
Pattern: hollow square
*****
*   *
*   *
*   *
*****
@author: KAILASH L M
"""
# Pattern: hollow square
n = int(input("Enter size: "))
for row in range(n):
    for column in range(n):
        if row in (0, n - 1) or column in (0, n - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

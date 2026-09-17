"""
Created on Thu Sep 17 21:06:26 2026
Pattern: star pyramid
    *
   ***
  *****
 *******
*********
@author: KAILASH L M
"""
# Pattern: star pyramid
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

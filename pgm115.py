"""
Created on Thu Sep 17 21:06:26 2026
Pattern: hollow triangle
    *
   * *
  *   *
 *******
@author: KAILASH L M
"""
# Pattern: hollow triangle
n = int(input("Enter number of rows: "))
for row in range(1, n + 1):
    print(" " * (n - row), end="")
    for column in range(1, 2 * row):
        if row == n or column in (1, 2 * row - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

"""
Created on Thu Sep 17 21:06:26 2026
Pattern: right aligned increasing stars
    *
   **
  ***
 ****
*****
@author: KAILASH L M
"""
# Pattern: right aligned increasing stars
n = int(input("Enter number of rows: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

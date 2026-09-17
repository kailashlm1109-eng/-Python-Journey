"""
Created on Thu Sep 17 21:06:26 2026
Pattern: left aligned decreasing stars
*****
****
***
**
*
@author: KAILASH L M
"""
# Pattern: left aligned decreasing stars
n = int(input("Enter number of rows: "))
for i in range(n, 0, -1):
    print("*" * i)

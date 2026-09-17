"""
Created on Thu Sep 17 21:06:26 2026
Menu-driven introduction to reusable functions
@author: KAILASH L M
"""
# Menu-driven introduction to reusable functions
def add(first, second):
    return first + second


def subtract(first, second):
    return first - second


def multiply(first, second):
    return first * second


print("1. Add")
print("2. Subtract")
print("3. Multiply")
choice = int(input("Choose an operation: "))
first = int(input("Enter first number: "))
second = int(input("Enter second number: "))

if choice == 1:
    print(add(first, second))
elif choice == 2:
    print(subtract(first, second))
elif choice == 3:
    print(multiply(first, second))
else:
    print("Invalid choice")

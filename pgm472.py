# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:58:37 2026
Menu pattern
@author: KAILASH L M
"""
def menu():
    print("1. N star")
    print("2. N by nstar")
    print("3. Right triangle")
    print("4. Invert right triangle")
    print("5. Right arrow triangle")
    print("6. Left space triangle")
    print("7. Minus star square")
    print("8. Star minus square")
    print("9. Minus star square triangle")
    print("10. Star minus squar triangle")
    print("11. Left arrow triangle")
    print("12. Right arrow space triangle")
    print("13. Pascal triangle")
    print("14. Invertpascal")
    print("15. Diamond")
    print("16. X star pattern")
    print("17. Diamond 123")
    print("18. X 123 pattern")
    print("19. Diamond abc")
    print("20. Hallo square")
    print("21. Right triangle star minus row")
    print("22. Right triangle star minus column")
    print("23. Pascal star minus")
    print("24. Hallo pascal triangle")
    print("25. Invert hallow pascal triangle")
    print("26. Hallow diamond")
    print("27. Exit")
    i = int(input("Enter Menu(1-27): "))
    return i

def n_star(r):
    print('*' * r)

def n_by_nstar(r):
    for i in range(r):
        print('*' * r)

def right_triangle(r):
    for i in range(1, r + 1):
        print('*' * i)

def InvertRightTriangle(r):
    for i in range(r, 0, -1):
        print('*' * i)

def rightArrowTriangle(r):
    for i in range(1, r + 1):
        print('*' * i)
    for i in range(r - 1, 0, -1):
        print('*' * i)

def leftSpaceTriangle(r):
    for i in range(r, 0, -1):
        print(' ' * (r - i) + '*' * i)
    for i in range(2, r + 1):
        print(' ' * (r - i) + '*' * i)


def minusStarSquare(r):
    for i in range(1, r + 1):
        print('-' * (r - i) + '*' * i)

def starMinusSquare(r):
    for i in range(r, 0, -1):
        print('-' * (r - i) + '*' * i)

def minusStarSquareTriangle(r):
    for i in range(1, r + 1):
        print('-' * (r - i) + '*' * i)
    for i in range(r - 1, 0, -1):
        print('-' * (r - i) + '*' * i)

def starMinusSquarTriangle(r):
    for i in range(r, 0, -1):
        print('-' * (r - i) + '*' * i)
    for i in range(2, r + 1):
        print('-' * (r - i) + '*' * i)

def leftArrowTriangle(r):
    for i in range(1, r + 1):
        print(' ' * (r - i) + '*' * i)
    for i in range(r - 1, 0, -1):
        print(' ' * (r - i) + '*' * i)

def rightArrowSpaceTriangle(r):
    for i in range(r, 0, -1):
        print(' ' * (r - i) + '*' * i)
    for i in range(2, r + 1):
        print(' ' * (r - i) + '*' * i)

def pascalTriangle(r):
    for i in range(1, r + 1):
        print(' ' * (r - i) + '*' * (2 * i - 1))

def invertpascal(r):
    for i in range(r, 0, -1):
        print(' ' * (r - i) + '*' * (2 * i - 1))

def diamond(r):
    for i in range(1, r + 1):
        print(' ' * (r - i) + '*' * (2 * i - 1))
    for i in range(r - 1, 0, -1):
        print(' ' * (r - i) + '*' * (2 * i - 1))

def xStarPattern(r):
    for i in range(r, 0, -1):
        print(' ' * (r - i) + '*' * (2 * i - 1))
    for i in range(2, r + 1):
        print(' ' * (r - i) + '*' * (2 * i - 1))

def diamond123(r):
    for i in range(1, r + 1):
        print(' ' * (r - i), end='')
        for x in range(1, (2 * i)):
            print(x, end='')
        print()
    for j in range(r - 1, 0, -1):
        print(' ' * (r - j), end='')
        for y in range(1, (2 * j)):
            print(y, end='')
        print()

def x123Pattern(r):
    for i in range(r, 0, -1):
        print(' ' * (r - i), end='')
        for x in range(1, (2 * i)):
            print(x, end='')
        print()
    for j in range(2, r + 1):
        print(' ' * (r - j), end='')
        for y in range(1, (2 * j)):
            print(y, end='')
        print()

def diamondAbc(r):
    for i in range(1, r + 1):
        print(' ' * (r - i) + chr(96 + i) * (2 * i - 1))
    for i in range(r - 1, 0, -1):
        print(' ' * (r - i) + chr(96 + i) * (2 * i - 1))

def halloSquare(r):
    print('*' * r)
    for i in range(1, r - 1):
        print('*' + ' ' * (r - 2) + '*')
    print('*' * r)

def rightTriangleStarMinusRow(r):
    for i in range(1, r + 1):
        if i % 2 == 1:
            print('*' * i)
        else:
            print('-' * i)

def rightTriangleStarMinusColumn(r):
    for i in range(1, r + 1):
        for j in range(i):
            if j % 2 == 0:
                print('*', end='')
            else:
                print('-', end='')
        print()

def pascalStarMinus(r):
    for i in range(1, r + 1):
        print(' ' * (r - i), end='')
        for j in range(i):
            if j == i - 1:
                print('*', end='')
            else:
                print('*-', end='')
        print()

def halloPascalTriangle(r):
    print(' ' * (r - 1) + '*')
    for i in range(2, r):
        print(' ' * (r - i) + '*' + ' ' * ((2 * i) - 2) + '*')
    print('*' * ((2 * r) - 1))

def invertHallowPascalTriangle(r):
    print('*' * ((2 * r) - 1))
    for i in range(r - 1, 1, -1):
        print(' ' * (r - i) + '*' + ' ' * ((2 * i) - 3) + '*')
    print(' ' * (r - 1) + '*')

def hallowDiamond(r):
    print(' ' * (r - 1) + '*')
    for i in range(2, r + 1):
        print(' ' * (r - i) + '*' + ' ' * ((2 * i) - 3) + '*')
    for j in range(r - 1, 1, -1):
        print(' ' * (r - j) + '*' + ' ' * ((2 * j) - 3) + '*')
    print(' ' * (r - 1) + '*')

# Main application flow
m = menu()
while m != 27:
    r = int(input("Enter Number of Rows: "))
    if m == 1:
        n_star(r)
    elif m == 2:
        n_by_nstar(r)
    elif m == 3:
        right_triangle(r)
    elif m == 4:
        InvertRightTriangle(r)
    elif m == 5:
        rightArrowTriangle(r)
    elif m == 6:
        leftSpaceTriangle(r)
    elif m == 7:
        minusStarSquare(r)
    elif m == 8:
        starMinusSquare(r)
    elif m == 9:
        minusStarSquareTriangle(r)
    elif m == 10:
        starMinusSquarTriangle(r)
    elif m == 11:
        leftArrowTriangle(r)
    elif m == 12:
        rightArrowSpaceTriangle(r)
    elif m == 13:
        pascalTriangle(r)
    elif m == 14:
        invertpascal(r)
    elif m == 15:
        diamond(r)
    elif m == 16:
        xStarPattern(r)
    elif m == 17:
        diamond123(r)
    elif m == 18:
        x123Pattern(r)
    elif m == 19:
        diamondAbc(r)
    elif m == 20:
        halloSquare(r)
    elif m == 21:
        rightTriangleStarMinusRow(r)
    elif m == 22:
        rightTriangleStarMinusColumn(r)
    elif m == 23:
        pascalStarMinus(r)
    elif m == 24:
        halloPascalTriangle(r)
    elif m == 25:
        invertHallowPascalTriangle(r)
    else:
        hallowDiamond(r)
    
    m = int(input("Enter Menu(1-27): "))
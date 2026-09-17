# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 11:07:11 2026
Menu slicing
@author: KAILASH L M
"""
def menu_string():
    print("1. Copy n characters")
    print("2. Copy all characters from nth position")
    print("3. Copy n character from mth position")
    print("4. Copy the last n character of string:")
    print("5. Reverse the text")
    print("6. Palindrome or not")
    print("7. Copy n character from right edge")
    print("8. Copy all character form nth postion (-ve")
    print("9. Copy n character from mth position (-ve")
    print("10. Copy last n character of the string")
    print("11. Exit")
    i=int(input("Enter Menu (1-11):"))
    return i
def copyNcharacter(s,n):
    s1=s[:n]
    return s1
def copyAllchrFromN(s,n):
    s1=s[n:]
    return s1
def copyNchrFromM(s,m,n):
    s1=s[m:m+n]
    return s1
def copyLastNchr(s,n):
    s1=s[len(s)-n:]
    return s1
def ReverseTheText(s):
    s1=s[::-1]
    return s1
def palindromeOrNot(s):
    s1=s[::-1]
    if s==s1:
        return "Palindrome"
    else:
        return "Not Palindrom"
def copyNcharacterFromRight(s,n):
    s1=s[-1:-n-1:-1]
    return s1
def copyAllchrFromN_Negative(s,n):
    s1=s[n::-1]
    return s1
def copyNchrFromM_Negative(s,m,n):
    l=len(s)-m
    s1=s[-l:-l-n-1:-1]
    return s1
def copyLastNchr_Negative(s,n):
    s1=s[-(len(s)-n)-1::-1]
    return s1

#main
m1=menu_string()
while m1!=11:
    s=input("Enter a string:")
    if m1==1:
        n=int(input("Enter no. of character:"))
        s1=copyNcharacter(s, n)
        print(s1)
    elif m1==2:
        n=int(input("Enter no. of character:"))
        s1=copyAllchrFromN(s, n)
        print(s1)
    elif m1==3:
        m=int(input("Enter a position of string:"))
        n=int(input("Enter no. of character:"))
        s1=copyNchrFromM(s, m, n)
        print(s1)
    elif m1==4:
        n=int(input("Enter no. of character:"))
        s1=copyLastNchr(s, n)
        print(s1)
    elif m1==5:
        s1=ReverseTheText(s)
        print(s1)
    elif m1==6:
        s1=palindromeOrNot(s)
        print(s1)
    elif m1==7:
        n=int(input("Enter no. of character:"))
        s1=copyNcharacterFromRight(s, n)
        print(s1)    
    elif m1==8:
        n=int(input("Enter no. of character:"))
        s1=copyAllchrFromN_Negative(s, n)
        print(s1)
    elif m1==9:
        n=int(input("Enter no. of character:"))
        m=int(input("Enter the postion of the character:"))
        s1=copyNchrFromM_Negative(s, m, n)
        print(s1)
    elif m1==10:
        n=int(input("Enter no. of character:"))
        s1=copyLastNchr_Negative(s, n)
        print(s1)
    else:
        print("Invalid Choice")
    m1=int(input("Enter Menu (1-11):"))
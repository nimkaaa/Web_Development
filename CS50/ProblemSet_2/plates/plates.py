"""
In plates.py, implement a program that prompts the user for a vanity plate and then output (Valid) if meets all of the requirements or (Invalid) if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).
"""
# 1) Start from 2 LETTERS (AA-XX-XX)
# 2) From 2 to 6 characters
# 3) After LETTERS come DIGITS
# 4) NO punctuation characters

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    length = len(s)
    if 2 <= length <= 6 and s.isalnum() and s[0:2].isalpha():
        if length == 2:
            return True
        elif s[2:length].isalpha():
            return True
        elif s[2:length].isdigit() and s[2] != "0":
            return True
        elif s[2].isalpha() and s[3:length].isdigit and s[3] != "0":
            return True
        elif s[2:length-2].isalpha() and s[4:length].isdigit() and s[4] != "0":
            return True
        elif s[3:length-1].isalpha() and s[5:length].isdigit() and s[5] != "0":
            return True
        elif s[4:length].isalpha() and s[6].isdigit() and s[6] != "0":
            return True
        else:
            return False
    else:
        return False


main()

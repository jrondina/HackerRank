# https://www.hackerrank.com/challenges/strong-password/problem

# !/bin/python3

import sys


def minimum_number(n, password):
    # Return the minimum number of characters to make the password strong
    new_chars = 0
    if not has_lower(password):
        new_chars += 1
    if not has_upper(password):
        new_chars += 1
    if not has_num(password):
        new_chars += 1

    if not has_special(password):
        new_chars += 1

    if n + new_chars >= 6:
        print(new_chars)
    else:
        print(6 - n)


def has_lower(password):
    for char in password:
        if char.islower():
            return True

    return False


def has_upper(password):
    for char in password:
        if char.isupper():
            return True

    return False


def has_num(password):
    for char in password:
        if char.isnumeric():
            return True

    return False



def has_special(password):
    special = "!@#$%^&*()-+"
    return len(set(password) & set(special)) > 0


n = int(input().strip())
password = input().strip()
answer = minimum_number(n, password)
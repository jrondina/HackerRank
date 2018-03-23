# https://www.hackerrank.com/challenges/day-of-the-programmer/problem\

leap = '12.09.'  # also gregorian leap
trans = '26.09.'
reg = '13.09.'


def is_julian(year):
    return 1700 <= year <= 1917


def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def solve(year):
    if year == 1918:
        return trans+str(year)
    elif (is_julian(year) and year % 4 == 0) or is_leap(year):
        return leap+str(year)
    else:
        return reg+str(year)


year = int(input().strip())
result = solve(year)
print(result)

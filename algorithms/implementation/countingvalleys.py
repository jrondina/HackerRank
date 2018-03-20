# https://www.hackerrank.com/challenges/counting-valleys/problem

def countingValleys(s):
    prev_el = 0
    elevation = 0
    is_valley = False
    vals = 0
    for char in s:
        if char == "U":
            prev_el = elevation
            elevation += 1
        else:
            prev_el = elevation
            elevation -= 1
        if not is_valley and elevation < 0:
            is_valley = True
            vals += 1
        if is_valley and elevation == 0 and prev_el < 0:
            is_valley = False

    print(vals)

n = input()
s = input().strip()
countingValleys(s)

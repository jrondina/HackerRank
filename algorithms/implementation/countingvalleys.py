# https://www.hackerrank.com/challenges/counting-valleys/problem

def countingValleys(s):
    elevation = 0
    is_valley = False
    vals = 0
    for char in s:
        if char == "U":
            elevation += 1
        else:
            elevation -= 1
        if not is_valley and elevation < 0:
            is_valley = True
        vals += 1
        if is_valley and elevation == 0:
            is_valley = False

    print(vals)


s = input().strip()
countingValleys(s)

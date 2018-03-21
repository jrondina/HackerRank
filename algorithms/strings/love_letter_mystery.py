def theLoveLetterMystery(s):
    total = 0
    for i in range(len(s)//2):
        total += abs(ord(s[i]) - ord(s[-i-1]))

    return total


q = int(input().strip())
for a0 in range(q):
    s = input().strip()
    result = theLoveLetterMystery(s)
    print(result)

# https://www.hackerrank.com/challenges/electronics-shop/problem


def getMoneySpent(keyboards, drives, s):
    total = 0
    if len(keyboards) < len(drives):
        for x in keyboards:
            for y in list(filter(lambda z: z >= min(drives) and z < s - x, drives)):
                if x + y == s:
                    return s
                elif x + y > s:
                    pass
                elif s > x + y > total:
                    total = x + y
                else:
                    pass
    else:
        for x in drives:
            for y in list(filter(lambda z: z >= min(keyboards) and z < s - x, keyboards)):
                if x + y == s:
                    return s
                elif x + y > s:
                    pass
                elif s > x + y > total:
                    total = x + y
                else:
                    pass
    if total > 0:
        return total
    else:
        return -1


s,n,m = input().strip().split(' ')
s,n,m = [int(s),int(n),int(m)]
keyboards = list(map(int, input().strip().split(' ')))
drives = list(map(int, input().strip().split(' ')))
#  The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
moneySpent = getMoneySpent(keyboards, drives, s)
print(moneySpent)

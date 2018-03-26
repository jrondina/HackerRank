# https://www.hackerrank.com/challenges/separate-the-numbers/problem


def separate_numbers(s):
    arr = list(s)
    print(combine_numbers(arr))


def combine_numbers(arr):
    new =[int(arr[0])]
    for i in range(1,len(arr)):
        if new[-1] < int(arr[i]):
            new.append(int(arr[i]))



    return new


if __name__ == "__main__":
    q = int(input().strip())
    for a0 in range(q):
        s = input().strip()
        separate_numbers(s)
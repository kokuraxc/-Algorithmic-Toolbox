# Uses python3

import sys


def custom_key(str):
    lenstr = len(str)
    return str * (4 // lenstr) + str[: 4 % lenstr]


def largest_number(a):
    # write your code here
    strlist = [str(_) for _ in a]
    strlist = sorted(strlist, key=custom_key, reverse=True)
    res = "".join(strlist)

    return res


if __name__ == "__main__":
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]

    # a = list(map(int, input().split()))
    print(largest_number(a))

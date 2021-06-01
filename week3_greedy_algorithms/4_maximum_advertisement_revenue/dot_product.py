# Uses python3

import sys


def max_dot_product(a, b):
    # write your code here
    a = sorted(a)
    b = sorted(b)
    return sum([_a * _b for _a, _b in zip(a, b)])
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    return res


if __name__ == "__main__":
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1 : (n + 1)]
    b = data[(n + 1) :]

    # a = map(int, input().split())
    # b = map(int, input().split())
    print(max_dot_product(a, b))

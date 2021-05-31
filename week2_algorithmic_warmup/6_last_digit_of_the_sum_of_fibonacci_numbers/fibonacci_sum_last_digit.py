# Uses python3
import sys


def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    # previous = 0
    # current  = 1
    # sum      = 1

    # for _ in range(n - 1):
    #     previous, current = current, previous + current
    #     sum += current

    # return sum % 10

    pre, cur, total = 0, 1, 1
    for _ in range(n - 1):
        pre, cur, total = cur, (pre + cur) % 10, (pre + cur + total) % 10
    return total


if __name__ == "__main__":
    input = sys.stdin.read()
    # input = input()
    n = int(input)
    print(fibonacci_sum_naive(n))

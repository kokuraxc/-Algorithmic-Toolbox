# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    m = fibonacci_sum_naive(from_ - 1)
    n = fibonacci_sum_naive(to)
    return (n - m) % 10


def fibonacci_sum_naive(n):
    if n == -1:
        return 0
    if n <= 1:
        return n

    pre, cur, total = 0, 1, 1
    for _ in range(n - 1):
        pre, cur, total = cur, (pre + cur) % 10, (pre + cur + total) % 10
    return total


if __name__ == "__main__":
    input = sys.stdin.read()
    # input = input()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))

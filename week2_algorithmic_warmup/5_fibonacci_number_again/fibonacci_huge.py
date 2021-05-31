# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def get_fib_w_remainder(n, m):
    rems = [0, 1]
    pre = 0
    cur = 1
    for _ in range(n - 1):
        pre, cur = cur, pre + cur
        rems.append(cur % m)
        if rems[-2:] == [0, 1]:
            rems = rems[:-2]
            break
    return rems[n % len(rems)]


if __name__ == "__main__":
    input = sys.stdin.read()
    # input = input()
    n, m = map(int, input.split())
    print(get_fib_w_remainder(n, m))

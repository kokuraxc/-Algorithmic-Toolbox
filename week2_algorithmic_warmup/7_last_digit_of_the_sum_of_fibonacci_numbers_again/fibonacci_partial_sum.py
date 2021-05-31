# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    m = get_fib_sum_last(from_ - 1)
    n = get_fib_sum_last(to)
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

def get_fib_rep(n, m):
    rems = [0, 1]
    pre = 0
    cur = 1
    for _ in range(n - 1):
        pre, cur = cur, pre + cur
        rems.append(cur % m)
        if rems[-2:] == [0, 1]:
            rems = rems[:-2]
            break
    return rems

def get_fib_sum_last(n):
    if n == -1:
        return 0
    if n <= 1:
        return n

    rems = get_fib_rep(n, 10)
    rep_rem = sum(rems) * ((n+1)//len(rems)) % 10
    rest_rem = sum(rems[:(n+1)%len(rems)]) % 10
    return (rep_rem + rest_rem) % 10

if __name__ == "__main__":
    # input = sys.stdin.read()
    input = input()
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_naive(from_, to))
    # print(get_fib_sum_last(from_))
    # print(get_fib_sum_last(to))

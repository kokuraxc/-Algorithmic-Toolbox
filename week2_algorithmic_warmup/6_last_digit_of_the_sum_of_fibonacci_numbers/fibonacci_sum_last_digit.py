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
    rems = get_fib_rep(n, 10)
    rep_rem = sum(rems) * ((n+1)//len(rems)) % 10
    rest_rem = sum(rems[:(n+1)%len(rems)]) % 10
    return (rep_rem + rest_rem) % 10
    

if __name__ == "__main__":
    # input = sys.stdin.read()
    input = input()
    n = int(input)
    print(get_fib_sum_last(n))

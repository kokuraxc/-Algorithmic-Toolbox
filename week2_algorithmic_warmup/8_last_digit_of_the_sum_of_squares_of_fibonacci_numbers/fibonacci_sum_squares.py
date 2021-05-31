# Uses python3
from sys import stdin


def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    fi_rems = [0, 1]
    # total_rems = [0, 1]
    square_total_rems = [0, 1]
    for _ in range(n - 1):
        fi_rems.append(sum(fi_rems[-2:]) % 10)
        # total_rems.append((total_rems[-1] + fi_rems[-1]) % 10)
        square_total_rems.append((square_total_rems[-1] + fi_rems[-1] ** 2) % 10)
        if fi_rems[-2:] == [0, 1]:
            fi_rems = fi_rems[-2:]
            square_total_rems = square_total_rems[-2:]
            break
    return square_total_rems[n % len(square_total_rems)]

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

def get_fib_square_sum_last(n):
    rems = get_fib_rep(n, 10)
    rems = [x ** 2 % 10 for x in rems]
    rep_rem = sum(rems) * ((n+1)//len(rems)) % 10
    rest_rem = sum(rems[:(n+1)%len(rems)]) % 10
    return (rep_rem + rest_rem) % 10

if __name__ == "__main__":
    # n = int(stdin.read())
    n = int(input())
    print(get_fib_square_sum_last(n))

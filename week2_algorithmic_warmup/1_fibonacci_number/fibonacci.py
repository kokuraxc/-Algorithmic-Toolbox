# Uses python3
def calc_fib(n):
    if n <= 1:
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)


def fibonacci(n):
    if n < 2:
        return n

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, previous + current
    return current


n = int(input())
print(fibonacci(n))

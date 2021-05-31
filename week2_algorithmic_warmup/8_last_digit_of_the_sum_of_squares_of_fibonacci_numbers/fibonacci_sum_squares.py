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


if __name__ == "__main__":
    n = int(stdin.read())
    # n = int(input())
    print(fibonacci_sum_squares_naive(n))

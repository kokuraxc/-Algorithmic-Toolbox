# Uses python3
import sys

def optimal_summands(n):
    assigned = 0
    summands = []
    cur = 1
    #write your code here
    while True:
        if cur + assigned > n:
            summands[-1] += n - assigned
            break
        summands.append(cur)
        assigned += cur
        cur += 1
    return summands

if __name__ == '__main__':
    # input = sys.stdin.read()
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')

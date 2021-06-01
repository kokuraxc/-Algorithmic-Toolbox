# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.0
    # write your code here
    unitValues = [value / weight for value, weight in zip(values, weights)]
    # convert list unitValues to dict
    unitValueDict = {k: v for k, v in enumerate(unitValues)}
    # print("before sorting: ", unitValueDict)
    # sort dict descedingly by value
    unitValueDict = dict(
        sorted(unitValueDict.items(), key=lambda item: item[1], reverse=True)
    )
    # print("after sorting: ", unitValueDict)
    # fill the capacity with weights by dict order
    for k in unitValueDict:
        w = min(capacity, weights[k])
        value += unitValueDict[k] * w
        capacity -= w
        if capacity == 0:
            break

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    # n, capacity = map(int, input().split())
    # values = list(map(int, input().split()))
    # # print(values)
    # weights = list(map(int, input().split()))
    # # print(weights)
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))

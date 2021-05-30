# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product, numbers[first] * numbers[second])

    return max_product


def getMax(nums):
    max1, idx = nums[0], 0
    for i, num in enumerate(nums):
        if num > max1:
            max1 = num
            idx = i
    return max1, idx


def max_pairwise_product_v2(nums):
    max1, idx = getMax(nums)
    max2, _ = getMax(nums[:idx] + nums[idx + 1 :])
    return max1 * max2


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_v2(input_numbers))

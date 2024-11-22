from collections import Counter


def main(nums):
    count = Counter(nums)
    max_len = 0
    for num in count:
        if num + 1 in count:
            max_len = max(max_len, count[num] + count[num + 1])

    return max_len

print(main([1, 3, 2, 2, 5, 2, 3, 7]))  # Output: 5

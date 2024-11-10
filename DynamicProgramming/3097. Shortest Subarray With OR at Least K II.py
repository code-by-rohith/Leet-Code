def main(nums, k):
    n = len(nums)
    min_len = float('inf')
    left = 0
    current_or = 0
    for right in range(n):
        current_or |= nums[right]
        while current_or >= k:
            min_len = min(min_len, right - left + 1)
            current_or ^= nums[left]
            left += 1
    return min_len if min_len != float('inf') else -1


# Test cases
print(main([1, 2, 3], 2))

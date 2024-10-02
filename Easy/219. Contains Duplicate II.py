def containsNearbyDuplicate(nums, k):
    num_map = {}

    for i, num in enumerate(nums):
        if num in num_map:
            if i - num_map[num] <= k:
                return True
        num_map[num] = i

    return False

print(containsNearbyDuplicate([1, 2, 3, 1], 3))
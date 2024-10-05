def containsNearbyDuplicate(nums, k):
    num_map = {}

    for i, num in enumerate(nums):
        if num in num_map:
            if i - num_map[num] <= k:
                return True
        num_map[num] = i

    return False

print(containsNearbyDuplicate([10, 27, 33, 27], 30))
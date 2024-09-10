def sortedSquares(nums):
    left = 0
    right = len(nums) - 1
    result = [0] * len(nums)
    index = len(nums) - 1
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[index] = nums[left] ** 2
            left += 1
        else:
            result[index] = nums[right] ** 2
            right -= 1
        index -= 1
    return result

print(sortedSquares(nums=[-5,-2,0,1,2,8,9,17]))
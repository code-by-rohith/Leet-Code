def main(nums):
    for i in range(len(nums)):
        arr = nums[:i] + nums[i+1:]
        count = 0
        for j in range(1, len(arr)):
            if arr[j] <= arr[j-1]:
                break
            else:
                count += 1
        if count == len(arr) - 1:
            return True
    return False
nums = [1, 2, 4,10,7]
print(main(nums))  # Output: True

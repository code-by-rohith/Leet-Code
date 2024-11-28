
def main(nums):
    if len(nums) == 1:
        return True

    for i in range(len(nums) - 1):
        if nums[i] & 1 == nums[i + 1] & 1:
            return False

    return True

print(main(nums = [2,1,2,2,2]))
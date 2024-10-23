from typing import List


def main(nums) :
        nums.sort()
        max_sum = sum(nums[i] for i in range(0, len(nums), 2))

        return max_sum



nums = [1,4,3,2]

print(main(nums))
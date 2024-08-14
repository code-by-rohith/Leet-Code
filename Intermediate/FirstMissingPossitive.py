from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        missing_positive = 1
        for num in nums:
            if num == missing_positive:
                missing_positive += 1

        return missing_positive

nums = [1, 2,3]
obj = Solution()
print(obj.firstMissingPositive(nums))

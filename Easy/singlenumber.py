
from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result
obj =Solution()
print(obj.singleNumber(nums=[1,5,8,8,1,3,2,3,2]))
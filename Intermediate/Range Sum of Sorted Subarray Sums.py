# Range Sum of Sorted Subarray Sums
"""
You are given the array nums consisting of n positive integers.
You computed the sum of all non-empty continuous subarrays from the array and
then sorted them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1), inclusive,
in the new array. Since the answer can be a huge number return it modulo 10^9 + 7.

Example 1:

Input: nums = [1,2,3,4], n = 4, left = 1, right = 5
Output: 13
Explanation: All subarray sums are 1, 3, 6, 10, 2, 5, 9, 3, 7, 4. A
fter sorting them in non-decreasing order we have the new array [1, 2, 3, 3, 4, 5, 6, 7, 9, 10].
The sum of the numbers from index left = 1 to right = 5 is 1 + 2 + 3 + 3 + 4 = 13.
"""



from typing import List
class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        res = []
        for i in range(n):
            x=0
            for j in range(i, n):
                x += nums[j]
                res.append(x)
        res.sort()
        return sum(res[left - 1:right]) % (10 ** 9 + 7)

nums = [1, 2, 3,4,5,6]
n = 6
left = 1
right = 5
obj=Solution()
print(obj.rangeSum(nums,n,left,right))
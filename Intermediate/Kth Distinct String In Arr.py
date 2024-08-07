"""
## A distinct string is a string that is present only once in an array.

## Given an array of strings arr, and an integer k, return the kth distinct string present in arr. If there are fewer than k distinct strings, return an empty string "".

## Note that the strings are considered in the order in which they appear in the array.

## Example 1:

## Input: arr =  ["d","b","c","b","c","a"], k = 2
## Output: "a"
## Explanation:
## The only distinct strings in arr are "d" and "a".
## "d" appears 1st, so it is the 1st distinct string.
## "a" appears 2nd, so it is the 2nd distinct string.
## Since k == 2, "a" is returned.
"""
from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        temp = []
        for i in arr:
            if count[i] == 1:
                temp.append(i)
        if len(temp) < k:
            return "none"
        else:
            return temp[k-1]
obj=Solution()
arr=["a","a","b","b","c","d"]
k=2
print((obj.kthDistinct(arr,2)))



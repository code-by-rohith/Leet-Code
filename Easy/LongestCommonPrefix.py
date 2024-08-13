#Longest Common Prefix

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res

strs =  ["flower","flowernnnnnnnnn","flower"]
obj=Solution()
print(obj.longestCommonPrefix(strs))


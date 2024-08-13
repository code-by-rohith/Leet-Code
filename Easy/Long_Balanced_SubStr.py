# You are given a binary string `s` consisting only of zeroes and ones.
#
# A substring of `s` is considered balanced if all zeroes are before ones
# and the number of zeroes is equal to the number of ones inside the substring.
# Notice that the empty substring is considered a balanced substring.
#
# Return the length of the longest balanced substring of `s`.
#
# A substring is a contiguous sequence of characters within a string.
#
# Example 1:
#
# Input: s = "01000111"
# Output: 6
# Explanation: The longest balanced substring is "000111", which has length 6.
#
# Example 2:
#
# Input: s = "00111"
# Output: 4
# Explanation: The longest balanced substring is "0011", which has length 4.


class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        best = 0
        c0, c1 = 0, 0

        for i in range(len(s)):
            if s[i] == '0':
                if c1 > 0:
                    c1 = 0
                    c0 = 1
                else:
                    c0 += 1
            else:
                c1 += 1
                best = max(best, 2 * min(c0, c1))

        return best

solution = Solution()
print(solution.findTheLongestBalancedSubstring("0000011111011"))


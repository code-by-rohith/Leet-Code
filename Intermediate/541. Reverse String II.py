class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        for i in range(0, len(s), 2 * k):
            result += s[i:i + k][::-1] + s[i + k:i + 2 * k]
        return result

solution = Solution()
print(solution.reverseStr("abcdefg", 2))
print(solution.reverseStr("abcd", 2))

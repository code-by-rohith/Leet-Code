class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        n = len(s)

        for i in range(0, n, 2 * k):
            temp = s[i:i + k][::-1]
            wamp = s[i + k:i + 2 * k]
            result += temp + wamp

        return result


solution = Solution()
print(solution.reverseStr("abcdefg", 2))
print(solution.reverseStr("abcd", 2))

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        stack = []
        for char in s:
            stack.append(char)
        for char in t:
            if stack and char in stack:
                stack.remove(char)
            else:
                return char

solution = Solution()
s1 = "abcd"
t1 = "abcde"
print(solution.findTheDifference(s1, t1))

s2 = ""
t2 = "y"
print(solution.findTheDifference(s2, t2))

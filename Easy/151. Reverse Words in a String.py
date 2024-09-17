class Solution:
    def reverseWords(self, s: str) -> str:
        samp = s.split()
        res = samp[::-1]
        return " ".join(res)

s="rohan is eating cake"
obj=Solution()
print(obj.reverseWords(s))
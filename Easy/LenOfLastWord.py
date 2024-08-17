class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        a = ""

        s = s.rstrip()
        if not s:
            return 0

        for i in s:
            if i != " ":
                a += i
            else:

                if a:
                    a = ""

        return len(a)




def reverseString(s):
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left = left + 1
            right = right - 1

s = ["h","e","l","l","o"]
reverseString(s)
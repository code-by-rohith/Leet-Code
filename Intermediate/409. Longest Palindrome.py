
def longestPalindrome(s):
    letters = {}
    for char in s:
        if char not in letters:
            letters[char] = 1
        else:
            letters[char] += 1
    res = 0
    odd_found = False
    for count in letters.values():
        if count % 2 == 0:
            res += count
        else:
            res += count - 1
            odd_found = True
    if odd_found:
        res += 1
    return res

s = "abccccdd"
print(longestPalindrome(s))
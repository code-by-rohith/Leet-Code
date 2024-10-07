def longestPalindrome(s: str) -> int:
    seen = set()
    res = 0

    for c in s:
        if c in seen:
            seen.remove(c)
            res += 2
        else:
            seen.add(c)

    return res + (1 if seen else 0)

print(longestPalindrome("abccccdd"))  # Output: 7

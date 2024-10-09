s = "pwwkew"
def main(s):
    a = set()
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            a.add(s[i:j])
    longest = ''
    for word in a:
        if len(word) > len(longest):
            if len(set(word)) == len(word):
                longest = word

    return  len(longest)

print(main(s))

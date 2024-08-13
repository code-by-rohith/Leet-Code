
def minimumDeletions(s: str) -> int:
    stack = []
    deletions = 0

    for char in s:
        if char == 'b':
            stack.append('b')
        elif char == 'a':
            if stack:
                stack.pop()
                deletions += 1

    return deletions

s="aaababbbba"
print(minimumDeletions(s))




def main(allowed,words):
    allowed=set(allowed)
    print(allowed)
    res=len(words)
    for c in words:
        for w in c:
            if w not in allowed:
                res -=1
                break
    return res

allowed = "abc"
words = ["ac","ba","aaab","baa","baab"]
print(main(allowed,words))
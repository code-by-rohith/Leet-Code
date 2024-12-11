
def main(a,b):
    if a == b:
        return -1
    return max(len(a), len(b))

a = "aba"
b = "cdd"
print(main(a,b))
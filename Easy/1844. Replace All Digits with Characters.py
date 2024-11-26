s = "a1c1e1"

def main(c,x):
    alp = "abcdefghijklmnopqrstuvwxyz"
    org = alp.index(c)
    return alp[org + x]
s = list(s)
for i in range(1, len(s), 2):
    s[i] = main(s[i - 1], int(s[i]))

print(''.join(s))


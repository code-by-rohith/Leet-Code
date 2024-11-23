def main(num):
    a = 0
    b = 0
    temp = num[::2]
    samp = num[1::2]
    for i in temp:
        a += int(i)
    for i in samp:
        b += int(i)
    return a == b

print(main('123456789'))
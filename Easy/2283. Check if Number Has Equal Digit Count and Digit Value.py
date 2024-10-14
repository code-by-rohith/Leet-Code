num = '1210'
def main(num):
    a = ''
    for i in range(len(num)):
        a += str(num.count(str(i)))
    return a == num

print(main(num))
s = "abacbc"
def main(s):
    count = {}
    for i in s:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)
    first_value = list(count.values())[0]
    res = True
    for count_value in count.values():
        if count_value != first_value:
            res = False
            break
    print(res)
main(s)

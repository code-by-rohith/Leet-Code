from collections import Counter
def main(nums):
    temp = Counter(nums)
    value = 0
    for i in temp.keys():
        if temp[i] == 1:
            value += i
    return value

print(main(nums = [1,2,3,2]))



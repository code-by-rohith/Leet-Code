def largestNumber(nums):
    array = list(map(str, nums))
    print(array)
    def compare(x):
        return x * 10
    array.sort(key=compare, reverse=True)
    print(array)
    if array[0] == "0":
        return "0"
    largest = ''.join(array)

    return largest


print(largestNumber([34, 30, 3, 9]))

a="30"
b="5"
print(a>b)
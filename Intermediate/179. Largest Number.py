def largestNumber(nums):
    array = list(map(str, nums))
    def compare(x):
        return x * 10
    array.sort(key=compare, reverse=True)
    if array[0] == "0":
        return "0"
    largest = ''.join(array)

    return largest


print(largestNumber([10, 2]))
print(largestNumber([3, 30, 34, 5, 9]))
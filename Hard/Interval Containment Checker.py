# arr = [[2, 5],[3,4] ]
# count = 0
#
# for i in range(len(arr)):
#     for j in range(len(arr)):
#         if i != j:
#             if arr[i][0] >= arr[j][0] and arr[i][1] <= arr[j][1]:
#                 count += 1
#                 break
#
# print(count)
def twoSum1(nums, target):
    arr = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                arr.append(i)
                arr.append(j)
                return arr  # return immediately after finding the first pair
    return arr  # return an empty list if no pair is found
nums = [3, 4, 8,4,2]
target = 6
result = twoSum1(nums, target)
print(result)





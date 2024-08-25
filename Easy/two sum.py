#
# def main(arr,k):
#     for i in range(len(arr)):
#         for j in range(i,len(arr)):
#             if arr[i] +arr[j] == k:
#                 print(i,j)
#
#
#
#
# arr=[8,9,6,5,1,5,6,78,98,95,2,687,5455]
# k=3
# main(arr,k)
def main(arr, k):
    seen = {}
    for i in range(len(arr)):
        complement = k - arr[i]
        if complement in seen:
            print(seen[complement], i)
        seen[arr[i]] = i

arr = [1,8,10,12,14,22,5,2,45]
k = 3
main(arr, k)


def method1(nums):

        n = len(nums)
        ans = 0
        for i in range(1, n + 1):
            ans ^= i
        for num in nums:
            ans ^= num
        return ans
nums=[0,1,2,3,4,5]
print(method1(nums))
num=[0,1,2,3,4,5]
def main(num):
    n=len(num)
    temp=0
    samp=0
    for i in range(1,n+1):
        temp += i
    for j in num:
        samp += j
    return temp - samp

print(main(num))



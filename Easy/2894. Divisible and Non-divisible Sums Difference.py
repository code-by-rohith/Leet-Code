# Input: n = 10, m = 3
# Output: 19
# Explanation: In the given example:
# - Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
# - Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
# We return 37 - 18 = 19 as the answer.
n=10
m=3

def main(m,n):
    count1 = 0
    count2 = 0
    for i in range(n+1):
        if i % m !=0:
            count1 += i
        if i % m ==0:
            count2 += i
    return  count1 -count2



print(main(m,n))


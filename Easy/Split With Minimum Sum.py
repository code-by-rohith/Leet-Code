# Given a positive integer num, split it into two non-negative integers num1 and num2 such that:
#
# The concatenation of num1 and num2 is a permutation of num.
# In other words, the sum of the number of occurrences of each digit in num1 and num2
# is equal to the number of occurrences of that digit in num.
# num1 and num2 can contain leading zeros.
# Return the minimum possible sum of num1 and num2.
#
# Notes:
#
# It is guaranteed that num does not contain any leading zeros.
# The order of occurrence of the digits in num1 and num2 may differ from the order of occurrence of num.


# Input: num = 4325
# Output: 59
# Explanation: We can split 4325 so that num1 is 24 and num2 is 35, giving a sum of 59.
# We can prove that 59 is indeed the minimal possible sum.


def split_min_sum(num):
    digits = sorted(str(num))
    num1, num2 = '', ''
    for i in range(len(digits)):
        if i % 2 == 0:
            num1 += digits[i]
        else:
            num2 += digits[i]
    num1 = int(num1)
    num2 = int(num2)

    return num1 + num2

print(split_min_sum(4325))
print(split_min_sum(12389))

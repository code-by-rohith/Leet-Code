"""
       Given an integer num, Bob will sneakily remap one of the 10 possible digits (0 to 9) to another digit.
       This function returns the difference between the maximum and minimum values Bob can make by remapping
       exactly one digit in num.

       Notes:
       - When Bob remaps a digit d1 to another digit d2, Bob replaces all occurrences of d1 in num with d2.
       - Bob can remap a digit to itself, in which case num does not change.
       - Bob can remap different digits for obtaining minimum and maximum values respectively.
       - The resulting number after remapping can contain leading zeroes.

       Example:
       Input: num = 11891
       Output: 99009
       Explanation:
       - To achieve the maximum value, Bob can remap the digit 1 to the digit 9 to yield 99899.
       - To achieve the minimum value, Bob can remap the digit 1 to the digit 0, yielding 890.
       - The difference between these two numbers is 99009.
       """
def maxDifference(num):
    num_str = str(num)

    max_num = num
    for digit in set(num_str):
        if digit != '9':
            max_num = max(max_num, int(num_str.replace(digit, '9')))
    min_num = num
    for digit in set(num_str):
        if digit != '0':
            min_num = min(min_num, int(num_str.replace(digit, '0')))

    return max_num - min_num


# Example usage
print(maxDifference(11891))
print(maxDifference(919))
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
print(maxDifference(11891))  # Output: 99009
print(maxDifference(919))  # Output: 99

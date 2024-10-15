def main(nums):
    closest = float('inf')
    for num in nums:
        if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
            closest = num
    return closest


nums = [-4, -2, 1, 4, 8]
print( main(nums))
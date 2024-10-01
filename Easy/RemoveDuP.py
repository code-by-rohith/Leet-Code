def main(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

    return None


print(main(nums=[1,2,3,4,4,4,5,8]))
def moain(nums):
    j= 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums

print(main(nums=[1,0,2,3,5,0,0,1]))
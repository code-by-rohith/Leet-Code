def main(nums):
    c=0
    for i in range(1,len(nums)):
        if nums[i]<=nums[i-1]:
            diff=nums[i-1]-nums[i]+1
            nums[i]=nums[i-1]+1
            c+=diff
    return c

print(main(nums = [1,5,2,4,1]))
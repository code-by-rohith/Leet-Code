def main(nums):
    count = 0
    temp=[]
    for i in range(0, len(nums)):
        count += nums[i]
        temp.append(count)
    return temp

nums= [1,2,3,4]
if __name__ == '__main__':
    main(nums)
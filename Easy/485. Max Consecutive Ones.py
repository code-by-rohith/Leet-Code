def main(nums):
        count = 0
        temp = 0
        for i in nums:
            if i != 1:
                count = 0

            else:
                count += 1
                temp = max(count, temp)
        return temp

print(main(nums=[1,1,1,0,0,1,1]))


def main(lower , upper , nums):
        nums.sort()
        count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if lower <= nums[i] + nums[j] <= upper:
                    count += 1
        return count

nums =[0,1,7,4,4,5]
lower =3
upper =6

print(main(lower,upper ,nums))
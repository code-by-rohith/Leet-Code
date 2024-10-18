nums = [3,2,1]
def main(nums):
    a = list(set(nums))
    b = sorted(a)
    if len(b) < 3:
        return b[-1]
    else:
        return b[-3]


print(main(nums))


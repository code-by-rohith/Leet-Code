
def permute(nums):
    if len(nums) == 0:
        return [[]]
    perms = permute(nums[1:])
    res = []
    for p in perms:
        for i in range(len(p) + 1):
            p_copy = p.copy()
            p_copy.insert(i, nums[0])
            res.append(p_copy)

    return res

print(permute([1,2,3]))
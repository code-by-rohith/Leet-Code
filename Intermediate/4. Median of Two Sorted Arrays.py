def main(nums1, nums2):
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    half_len = (m + n + 1) // 2
    while left <= right:
        i = (left + right) // 2
        j = half_len - i
        if i < m and nums1[i] < nums2[j - 1]:
            left = i + 1
        elif i > 0 and nums1[i - 1] > nums2[j]:
            right = i - 1
        else:
            if i == 0:
                max_of_left = nums2[j - 1]
            elif j == 0:
                max_of_left = nums1[i - 1]
            else:
                max_of_left = max(nums1[i - 1], nums2[j - 1])

            if (m + n) % 2 == 1:
                return max_of_left
            if i == m:
                min_of_right = nums2[j]
            elif j == n:
                min_of_right = nums1[i]
            else:
                min_of_right = min(nums1[i], nums2[j])

            return (max_of_left + min_of_right) / 2.0

nums1 = [1, 3]
nums2 = [2]
print(main(nums1,nums2))
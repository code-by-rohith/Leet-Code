from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        for i in arr:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        temp = []
        for i in arr:
            if count[i] == 1:
                temp.append(i)
        if len(temp) < k:
            return "none"
        else:
            return temp[k-1]
obj=Solution()
arr=["a","a","b","b","c"]
k=2
print((obj.kthDistinct(arr,1)))



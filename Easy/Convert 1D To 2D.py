import numpy as np
from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        temp = np.array(original)
        newarr = temp.reshape(m, n)

        return newarr.tolist()


original=[5,8,6,4,2]
obj =Solution()
print(obj.construct2DArray(original,5,1))
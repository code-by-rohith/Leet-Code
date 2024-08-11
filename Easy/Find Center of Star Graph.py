from typing import List

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]
solution = Solution()

edges1 = [[1, 2], [2, 3], [4, 2]]
print(solution.findCenter(edges1))

edges2 = [[1, 2], [5, 1], [1, 3], [1, 4]]
print(solution.findCenter(edges2))

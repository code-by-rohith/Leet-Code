
from typing import List
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        ret = 0
        for row in range(len(grid)-2):
            for col in range(len(grid[0])-2):
                numbers = []
                z = set()
                temp1 = []
                temp2 = []
                for x in range(3):
                    temp1.append(grid[row+x][col+x])
                    temp2.append(grid[row+2-x][col+x])
                z.add(sum(temp1))
                z.add(sum(temp2))
                for x in range(3):
                    temp1 = []
                    temp2 = []
                    for y in range(3):
                        numbers.append(grid[row+x][col+y])
                        temp1.append(grid[row+x][col+y])
                        temp2.append(grid[row+y][col+x])
                    z.add(sum(temp1))
                    z.add(sum(temp2))
                if len(z) == 1 and sorted(numbers) == [i+1 for i in range(9)]:
                    ret += 1
        return ret

grid1 = [[4, 3, 8, 4],
         [9, 5, 1, 9],
         [2, 7, 6, 2]]

sol = Solution()
print(sol.numMagicSquaresInside(grid1))



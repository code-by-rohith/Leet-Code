


def findColumnWidth(grid):
    m = len(grid)
    n = len(grid[0])

    column_widths = [0] * n
    for col in range(n):
        max_width = 0
        for row in range(m):
            length = len(str(grid[row][col]))
            if length > max_width:
                max_width = length
        column_widths[col] = max_width

    return column_widths


print(findColumnWidth([[-15, 1, 3], [15, 7, 12], [5, 6, -2]]))


#method 2 -inbuilt

from typing import List

class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        return [max(len(str(x)) for x in col) for col in zip(*grid)]

# Test cases
solution = Solution()
print(solution.findColumnWidth([[1], [22], [333]]))  # Output: [3]
print(solution.findColumnWidth([[-15, 1, 3], [15, 7, 12], [5, 6, -2]]))  # Output: [3, 1, 2]

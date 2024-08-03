# 2639. Find the Width of Columns of a Grid
# Solved Easy
#
# You are given a 0-indexed m x n integer matrix grid.
# The width of a column is the maximum length of its integers.
#
# For example, if grid = [[-10], [3], [12]], the width of the only column is 3 since -10 is of length 3.
# Return an integer array ans of size n where ans[i] is the width of the ith column.
#
# The length of an integer x with len digits is equal to len if x is non-negative, and len + 1 otherwise.
#
# Input: grid = [[-15, 1, 3], [15, 7, 12], [5, 6, -2]]
# Output: [3, 1, 2]
# Explanation:
# In the 0th column, only -15 is of length 3.
# In the 1st column, all integers are of length 1.
# In the 2nd column, both 12 and -2 are of length 2.

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

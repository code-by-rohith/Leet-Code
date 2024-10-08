# 1572. Matrix Diagonal Sum

# Given a square matrix mat, return the sum of the matrix diagonals.
#
# Only include the sum of all the elements on the primary diagonal and
# all the elements on the secondary diagonal that are not part of the primary diagonal.
# Input: mat = [[1,2,3],
#               [4,5,6],
#               [7,8,9]]
# Output: 25
# Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
# Notice that element mat[1][1] = 5 is counted only once.
# Example 2:
#
# Input: mat = [[1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1],
#               [1,1,1,1]]
# Output: 8
# Example 3:
#
# Input: mat = [[5]]
# Output: 5

from typing import List


def diagonal_sum(mat):
    res, n = 0, len(mat)
    for i in range(n):
        res += mat[i][i]
        res += mat[i][n - 1 - i]
    return res - (mat[n // 2][n // 2] if n % 2 else 0)


# Example usage
mat1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonal_sum(mat1))

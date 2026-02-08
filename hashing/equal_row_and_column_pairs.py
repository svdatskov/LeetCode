# Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.
#
# A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
#
#
#
# Example 1:
#
#
# Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
# Output: 1
# Explanation: There is 1 equal row and column pair:
# - (Row 2, Column 1): [2,7,7]
# Example 2:
#
#
# Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
# Output: 3
# Explanation: There are 3 equal row and column pairs:
# - (Row 0, Column 0): [3,1,2,2]
# - (Row 2, Column 2): [2,4,2,2]
# - (Row 3, Column 2): [2,4,2,2]
#
#
# Constraints:
#
# n == grid.length == grid[i].length
# 1 <= n <= 200
# 1 <= grid[i][j] <= 105
from typing import List
from collections import defaultdict


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        def convert_to_dict_key(arr: List[int]) -> tuple:
            return tuple(arr)

        row_dict = defaultdict(int)

        for row in grid:
            row_dict[convert_to_dict_key(row)] += 1

        column_dict = defaultdict(int)
        grid_size = len(grid[0])

        for i in range(grid_size):
            column = []

            for row in grid:
                column.append(row[i])

            column_dict[convert_to_dict_key(column)] += 1

        ans = 0

        for column in column_dict:
            ans += column_dict[column] * row_dict[column]

        return ans





s = Solution()
print(s.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))


# [[3,2,1],[1,7,6],[2,7,7]]

# { 0: [3,1,2], 1: [2,7,7], 2: [1,6,7]}
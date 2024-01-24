# Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.
# Note: You can only move either down or right at any point in time.


# Example 1:

# Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
# Output: 7
# Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

# Example 2:

# Input: grid = [[1,2,3],[4,5,6]]
# Output: 12


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 200
# 0 <= grid[i][j] <= 200


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # Graph-style problem. We want to traverse to the end, finding the minimum sum path.
        # We can only go to the right or down at any point.

        # Key takeaway: Traverse the grid, and at each cell add the minimum of the cell to the left or above.
        rows = len(grid)
        cols = len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if r == 0 and c > 0:
                    grid[r][c] += grid[r][c - 1]
                elif c == 0 and r > 0:
                    grid[r][c] += grid[r - 1][c]
                elif r > 0 and c > 0:
                    grid[r][c] += min(grid[r - 1][c], grid[r][c - 1])

        return grid[rows - 1][cols - 1]

# Time Complexity: O(m * n) -> One pass of m * n matrix
# Space Complexity: O(m * n) -> All values stored in a single m * n matrix
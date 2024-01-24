# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.
# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The test cases are generated so that the answer will be less than or equal to 2 * 109.


# Example 1:


# Input: m = 3, n = 7
# Output: 28
# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down


# Constraints:

# 1 <= m, n <= 100


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Grid-style problem. Want to traverse the grid and determine how many paths lead to final cell in bottom right.
        # Want to traverse the grid, left to right and top to bottom.
        # First cell will have a value of 1 (1 path to step onto the board / start the game).

        grid = [[0] * n for i in range(m)]
        grid[0][0] = 1

        # Start traversal and add the value from the cell to immediate left. Also add the value from cell immediately above.

        for i in range(m):
            for j in range(n):
                if i > 0:
                    grid[i][j] += grid[i - 1][j]
                if j > 0:
                    grid[i][j] += grid[i][j - 1]

        # Result will be the # of paths that reach the final cell.

        return grid[m - 1][n - 1]


# Time Complexity: O(m * n) => One traversal over the entire m * n grid
# Space Complexity: O(m * n) => Storing objects on a single m * n grid
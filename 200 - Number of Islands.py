# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.


# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1

# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3


# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Want to count # islands -> Basically, we want to count how many separate contiguous "land" masses there are.
        # Achieve this with a DFS. For each DFS, transform every "1" cell visited into a "0". Then incremement count by 1.

        count = 0

        def dfs(row, col):
            # Valid square and value is "1".
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == "1":
                grid[row][col] = "0"
                dfs(row + 1, col)
                dfs(row - 1, col)
                dfs(row, col + 1)
                dfs(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)

        return count


# Time Complexity: O(n * m) -> Visit every cell at most 1 time.
# Space Complexity: O(1) -> No additional storage.


# 2nd Solution:

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Return the number of islands in the grid.
        # DFS-style solution -> as we visit land, we can immediately transform it to a "0" to avoid re-counting.

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] == "0":
                return
            grid[row][col] = "0"
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        num_islands = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    num_islands += 1
                    dfs(row, col)

        return num_islands

# Time Complexity: O(n * m) -> Visit each cell in 2D array once.
# Space Complexity: O(n * m) -> Store recursive calls on stack equal to # of "land" cells.

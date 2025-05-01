# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
# The area of an island is the number of cells with a value 1 in the island.
# Return the maximum area of an island in grid. If there is no island, return 0.


# Example 1:

# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # We can traverse the entire grid and perform a DFS when we reach a "1".
        # For each new "1" that we visit, we can try to expand up/down/left/right to find connected land.
        # Tranform cells as they are visited, that way we don't visit them again in a later DFS.

        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return 0
            if grid[row][col] != 1:
                return 0
            grid[row][col] = 0
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    islandCount = dfs(i, j)
                    res = max(res, islandCount)

        return res

# Time Complexity: O(m * n) -> Traverse the entire grid, visiting each cell once.
# Space Complexity: O(L) -> L is size of largest island -> call stack may contain up to L calls for each cell in island.


# Solution 2:

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Traverse the matrix, and for each unseen 1 -> DFS to capture all connected 1's.

        seen = set()  # Contains (r, c) for each seen island
        max_island_size = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or (row, col) in seen or grid[row][col] != 1:
                return 0

            # Case where island is an unvisited 1.
            seen.add((row, col))
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                cur_island_size = dfs(row, col)
                max_island_size = max(max_island_size, cur_island_size)

        return max_island_size

# Time Complexity: O(n * m) -> Traverse entire grid and visit each cell exactly one time.
# Space Complexity: O(n * m) -> In seen set, store all coordinates of visited island cells. In worst case, every cell is an island.

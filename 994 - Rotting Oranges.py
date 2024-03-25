# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

# Example 1:

# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # BFS of each orange that is rotten in the grid. We want to see how many minutes it takes to reach every orange.

        q = deque()
        count = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r + 1, c))
                    q.append((r - 1, c))
                    q.append((r, c + 1))
                    q.append((r, c - 1))
                if grid[r][c] == 1:
                    count += 1

        if count == 0:
            return 0

        # Now, we know the count of fresh oranges, and the location of each rotten orange (on stack). BFS the rotten oranges on the stack.
        timeTaken = 0
        while q:
            qLength = len(q)
            timeTaken += 1
            for i in range(qLength):
                curRow, curCol = q.popleft()
                if 0 <= curRow < len(grid) and 0 <= curCol < len(grid[0]) and grid[curRow][curCol] == 1: # Fresh orange, ready to make rot.
                    count -= 1
                    grid[curRow][curCol] = 2
                    q.append((curRow + 1, curCol))
                    q.append((curRow - 1, curCol))
                    q.append((curRow, curCol + 1))
                    q.append((curRow, curCol - 1))
            if count == 0:
                return timeTaken


        return -1

# Time Complexity: O(n * m) -> We visit every cell in the grid up to 2 times (once for counting initially, and once during traversal/BFS).
# Space Complexity: O(n * m) -> Store on stack, up to every cell on the grid.
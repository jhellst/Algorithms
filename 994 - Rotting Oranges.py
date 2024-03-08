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
        # Grid cells are 1) empty, 2) fresh orange, or 3) rotten orange.
        # We want to see how long it takes for every orange to be rotten. Every rotten orange "spreads" the rot to all adjacent fresh oranges each turn.

        # BFS-style solution: We want to rot the oranges, second by second.
        # For each rotten orange, we want to BFS the surrounding oranges to rot them.

        q = deque()
        timeTaken = 0
        orangeCount = 0

        # First, traverse the grid and find every rotten orange to start.
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    orangeCount += 1

        if orangeCount == 0:
            return timeTaken

        # Now, we can run BFS on each rotten orange. Each time we deplete the queue, increment time by 1.
        while q:
            timeTaken += 1
            qLen = len(q)
            for i in range(qLen):
                curX, curY = q.popleft() # Now we want to add all adjacent fresh oranges to queue.

                candidates = [(curX + 1, curY), (curX - 1, curY), (curX, curY + 1), (curX, curY - 1)] # Adjacent cells
                for x, y in candidates:
                    if x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0]) and grid[x][y] == 1: # Valid cell is 1) in range and 2) contains a fresh orange.
                        grid[x][y] = 2
                        orangeCount -= 1
                        q.append((x, y))
                        if orangeCount == 0:
                            return timeTaken

        return -1

# Time Complexity: O(n * m) -> We visit every cell in the grid up to 2 times (once for counting initially, and once during traversal/BFS).
# Space Complexity: O(n * m) -> Store on stack, up to every cell on the grid.
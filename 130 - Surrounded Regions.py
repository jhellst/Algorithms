# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:
# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board.

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# Explanation:
# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

# Example 2:

# Input: board = [["X"]]
# Output: [["X"]]


# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.




class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Transorm the board, DFS-style, to capture surrounded regions that don't touch the edge.
        #   - On DFS, transform "O" vals to "Z" -> This will prevent them from being transformed again in the DFS process.

        rows, cols = len(board), len(board[0])

        # Now, we can DFS from the edge to "capture" any land regions that touch the edge (start with a "Z").
        def dfs(r, c):
            print(r, c)
            if r >= 0 and r < rows and c >= 0 and c < cols: # Valid cell.
                if board[r][c] == "O":
                    board[r][c] = "Z"
                    dfs(r + 1, c)
                    dfs(r - 1, c)
                    dfs(r, c + 1)
                    dfs(r, c - 1)

        # Traverse the edges and DFS inwards from any "Z" value.
        for r in range(rows):
            dfs(r, 0)
            dfs(r, cols - 1)
        for c in range(cols):
            dfs(0, c)
            dfs(rows - 1, c)

        # Transform O -> X and Z -> O
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "Z":
                    board[r][c] = "O"
                else:
                    board[r][c] = "X"


# Time Complexity: O(n) -> Visit every cell up to twice.
# Space Complexity: O(n) -> Store recursive DFS calls up to every cell in the array.
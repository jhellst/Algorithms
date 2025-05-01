# Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.
# Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k(1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships(i.e., there are no adjacent battleships).

# Example 1:
# Input: board = [["X", ".", ".", "X"], [
#     ".", ".", ".", "X"], [".", ".", ".", "X"]]
# Output: 2

# Example 2:
# Input: board = [["."]]
# Output: 0

# Constraints:
#     m == board.length
#     n == board[i].length
#     1 <= m, n <= 200
#     board[i][j] is either '.' or 'X'.


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # Count every battleship.
        # Key Details:
        #   1) No adjacent battleships (at least one water space between any ships).
        #   2) Dimensions of ship -> 1 * k -> where k can be any int > 0.

        # Because no ships border one-another, we can actually just transform the cells (into "." or another char) as we visit them.
        #   - This will save space (otherwise, we'd use a set).

        # DFS-style solution.
        num_ships = 0

        def dfs(row, col):
            if row < 0 or col < 0 or row >= len(board) or col >= len(board[0]) or board[row][col] != "X":
                return False
            board[row][col] = "."
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)
            return True

        for row in range(len(board)):
            for col in range(len(board[0])):
                if dfs(row, col):
                    num_ships += 1

        return num_ships

# Time Complexity: O(n * m) -> Visit each cell on board once.
# Space Complexity: O(1) -> No additional storage space used.

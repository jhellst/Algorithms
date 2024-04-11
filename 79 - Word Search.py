# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Example 2:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Example 3:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

# Constraints:

# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.

# Follow up: Could you use search pruning to make your solution faster with a larger board?

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFS of the board. Want to return true if the word can ever be constructed from adjacent, non-repeating cells.

        rows, cols = len(board), len(board[0])
        seen = set()

        def dfs(row, col, index):
            if index >= len(word): # End of word.
                return True
            elif row < 0 or col < 0 or row >= rows or col >= cols or (row, col) in seen or board[row][col] != word[index]: # Cell not in range, visited, or not a match.
                return False

            # In all other cases, the cell contains the correct value.
            seen.add((row, col))
            res = dfs(row + 1, col, index + 1) or dfs(row - 1, col, index + 1) or dfs(row, col + 1, index + 1) or dfs(row, col - 1, index + 1)
            seen.remove((row, col))
            return res

        for r in range(rows):
            for c in range(cols):
                wordFound = dfs(r, c, 0)
                if wordFound:
                    return True

        return False

# Time Complexity: O(m * n * dfs) -> O(m * n * 4^w) -> Traverse all rows and cols, then dfs in 4 directions at each point. (w is len(word))
# Space Complexity: O(n) -> Store up to each cell once in set.
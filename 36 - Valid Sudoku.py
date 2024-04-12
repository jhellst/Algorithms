# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:

# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true

# Example 2:

# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.


# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Validate the board. Need to check all possible groupings to ensure that none have duplicates.
        # Up, down, square -> these are groupings to check for.
        # Square can contain "." or a number.

        rows = len(board)
        cols = len(board[0])

        rowValues, colValues = {}, {} # index:set(values)
        squareValues = {} # (coords):set(values)

        # First, check horizontal and vertical (at the same time).
        # Also check for each square.

        for r in range(rows):
            for c in range(cols):

                curVal = board[r][c]
                if curVal != ".": # Blank space doesn't need to be checked for validity.

                    # Check repeated values in row.
                    if r in rowValues:
                        if curVal in rowValues[r]:
                            return False
                        rowValues[r].add(curVal)
                    else:
                        rowValues[r] = set()
                        rowValues[r].add(curVal)

                    # Check repeated values in col.
                    if c in colValues:
                        if curVal in colValues[c]:
                            return False
                        colValues[c].add(curVal)
                    else:
                        colValues[c] = set()
                        colValues[c].add(curVal)

                    # Use integer division to determine the specific square that we're within. Coords represented by (rowIndex % 3, colIndex % 3)
                    squareIndices = (r // 3, c // 3)

                    # Check repeated values in square.
                    if squareIndices in squareValues:
                        if curVal in squareValues[squareIndices]:
                            return False
                        squareValues[squareIndices].add(curVal)
                    else:
                        squareValues[squareIndices] = set()
                        squareValues[squareIndices].add(curVal)

        return True

# Time Complexity: O(n) -> Visit every cell in 2D array exactly once.
# Space Complexity: O(3n) -> O(n) -> Store every value in a set exactly 3 times (if != ".").
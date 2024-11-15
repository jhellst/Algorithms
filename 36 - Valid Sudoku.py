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



# 2nd Solution:

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # A valid board needs to meet all of the requirements for a valid Sudoku game:
        #   - Each square has no repeat values.
        #   - Each row has no repeat values.
        #   - Each column has no repeat values.
        #   - Ignoring final rule that diagonals are also checked.

        # Use sets to check each "grouping" for duplicate values.
        # As we traverse each cell, we'll add to all 3 groupings to check validity.
        rows = {} # row: set(nums)
        cols = {} # col: set(nums)
        squares = {} # (row // 3, col // 3): set(nums)

        for row in range(len(board)):
            for col in range(len(board[0])):

                cur_val = board[row][col]
                if cur_val != ".":

                    if row in rows:
                        if cur_val in rows[row]:
                            return False
                        rows[row].add(cur_val)
                    else:
                        rows[row] = set()
                        rows[row].add(cur_val)

                    if col in cols:
                        if cur_val in cols[col]:
                            return False
                        cols[col].add(cur_val)
                    else:
                        cols[col] = set()
                        cols[col].add(cur_val)

                    square_indices = (row // 3, col // 3)
                    if square_indices in squares:
                        if cur_val in squares[square_indices]:
                            return False
                        squares[square_indices].add(cur_val)
                    else:
                        squares[square_indices] = set()
                        squares[square_indices].add(cur_val)

        return True

# Time Complexity: O(n * m) -> Visit every cell in the matrix once.
# Space Complexity: O(3 * n * m) -> O(n * m) -> Store values in dictionaries -> In worst case, each cell's value will be stored 3 times.
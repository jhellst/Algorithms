# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.

# Example 1:

# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:

# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1

# Follow up:

# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Modify the matrix in-place. For every 0, change the entire row and column to 0.

        rows, cols = set(), set() # Sets to hold the rows, cols to transform.
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rows.add(r)
                    cols.add(c)

        for r in rows:
            for c in range(len(matrix[0])):
                matrix[r][c] = 0
        for c in cols:
            for r in range(len(matrix)):
                matrix[r][c] = 0

# Time Complexity: O( m * n ) -> Traversal of matrix, then second traversal to transform.
# Space Complexity: O(m + n) -> Sets may hold every row and every column once.




# 2nd Solution:

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # For any row or column with a zero -> set every cell to 0.
        #   - Simple idea: Use a dict/set data structure to store every row/col with a zero.

        rows = set()
        cols = set()

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                cur_val = matrix[row][col]
                if cur_val == 0:
                    rows.add(row)
                    cols.add(col)

        # Now, modify all rows/cols that contained a zero -> all cells will now be transformed to 0.
        for row in rows:
            for col in range(len(matrix[0])):
                matrix[row][col] = 0
        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col] = 0

# Time Complexity: O(n * m) -> Visit every cell in matrix once.
# Space Complexity: O(n + m) -> Store in sets, in worst case will store every row and every column once.
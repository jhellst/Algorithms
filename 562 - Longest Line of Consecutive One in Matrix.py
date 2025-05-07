# Given an m x n binary matrix mat, return the length of the longest line of consecutive one in the matrix.
# The line could be horizontal, vertical, diagonal, or anti-diagonal.

# Example 1:
# Input: mat = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 1]]
# Output: 3

# Example 2:
# Input: mat = [[1, 1, 1, 1], [0, 1, 1, 0], [0, 0, 0, 1]]
# Output: 4


# Constraints:
#     m == mat.length
#     n == mat[i].length
#     1 <= m, n <= 104
#     1 <= m * n <= 104
#     mat[i][j] is either 0 or 1.


class Solution:
    def longestLine(self, mat: List[List[int]]) -> int:
        # Find the length of the longest consecutive group of 1's.
        #   - Horizontal, Vertical, or Diagonal.

        # Key Concept: From each zero, "DFS" to expand and check all consecutive 1's.
        #   - Key Detail: We only have to count left->right, top->bottom, and both diagonals.

        def check_consecutive(row, col):
            horizontal_count = 0
            if 0 <= row < len(mat) and 0 <= col < len(mat[0]) and mat[row][col] == 1:
                # 1) Count horizontally to the right. Can avoid this step if there's a 1 directly to the left.
                horizontal_count += 1
                if not (col != 0 and mat[row][col - 1] == 1):
                    for c in range(col + 1, len(mat[0])):
                        if mat[row][c] == 1:
                            horizontal_count += 1
                        else:
                            break

            vertical_count = 0
            if 0 <= row < len(mat) and 0 <= col < len(mat[0]) and mat[row][col] == 1:
                vertical_count += 1
                if not (row != 0 and mat[row - 1][col] == 1):
                    for r in range(row + 1, len(mat)):
                        if mat[r][col] == 1:
                            vertical_count += 1
                        else:
                            break

            lr_diagonal_count = 0
            if 0 <= row < len(mat) and 0 <= col < len(mat[0]) and mat[row][col] == 1:
                lr_diagonal_count += 1
                if not (row != 0 and col != 0 and mat[row - 1][col - 1] == 1):
                    r, c = row + 1, col + 1
                    while r < len(mat) and c < len(mat[0]):
                        if mat[r][c] == 1:
                            lr_diagonal_count += 1
                            r += 1
                            c += 1
                        else:
                            break

            rl_diagonal_count = 0
            if 0 <= row < len(mat) and 0 <= col < len(mat[0]) and mat[row][col] == 1:
                rl_diagonal_count += 1
                if not (row != 0 and col != len(mat[0]) - 1 and mat[row - 1][col + 1] == 1):
                    r, c = row + 1, col - 1
                    while r < len(mat) and c >= 0:
                        print(r, c)
                        if mat[r][c] == 1:
                            rl_diagonal_count += 1
                            r += 1
                            c -= 1
                        else:
                            break

            return max(horizontal_count, vertical_count, lr_diagonal_count, rl_diagonal_count)

        max_count = 0

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                if mat[row][col] == 1:
                    max_count = max(max_count, check_consecutive(row, col))

        return max_count

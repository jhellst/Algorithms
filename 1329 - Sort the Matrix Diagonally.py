# A matrix diagonal is a diagonal line of cells starting from some cell in either the topmost row or leftmost column and going in the bottom-right direction until reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].
# Given an m x n matrix mat of integers, sort each matrix diagonal in ascending order and return the resulting matrix.

# Example 1:

# Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
# Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

# Example 2:

# Input: mat = [[11,25,66,1,69,7],[23,55,17,45,15,52],[75,31,36,44,58,8],[22,27,33,25,68,4],[84,28,14,11,5,50]]
# Output: [[5,17,4,1,52,7],[11,11,25,45,8,69],[14,23,25,44,58,15],[22,27,31,36,50,66],[84,28,75,33,55,68]]


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        # Given the original array, we want to sort the diagnals by size. Work from top-left to bottom-right.

        # Traverse each diagonal and sort it (or use heap) -> Then, traverse the same diagonal to insert the sorted vals in order.
        # Diagonals of length 1 are already sorted.

        rows, cols = len(mat), len(mat[0])
        if not mat or rows <= 1 or cols <= 1:
            return mat

        for r in range(rows - 1, -1, -1): # Traverse rows from index 1 to rows - 1
            curRow = r
            curCol = 0
            curDiag = [] # Stores diagonal, to be later sorted.
            while curCol < cols and curRow < rows:
                curDiag.append(mat[curRow][curCol])
                curRow += 1
                curCol += 1
            curDiag.sort()
            # Now, traverse the same diagonal again and add back the values, this time from the sorted array.
            curRow = r
            curCol = 0
            for val in curDiag:
                mat[curRow][curCol] = val
                curRow += 1
                curCol += 1

        for c in range(1, cols): # Traverse cols from index 1 to cols - 1.
            curCol = c
            curRow = 0
            curDiag = [] # Stores diagonal, to be later sorted.
            while curCol < cols and curRow < rows:
                curDiag.append(mat[curRow][curCol])
                curRow += 1
                curCol += 1
            curDiag.sort()
            # # Now, traverse the same diagonal again and add back the values, this time from the sorted array.
            curRow = 0
            curCol = c
            for val in curDiag:
                mat[curRow][curCol] = val
                curRow += 1
                curCol += 1

        return mat

# Time Complexity: O(m * n * log(min(m, n))) -> Traverse every diagonal, then sort the array of the diagonal (whose max length is min(m, n)).
# Space Complexity: O(min(m, n)) -> Store Up to one diagonal at a time.
# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Constraints:
#     m == matrix.length
#     n == matrix[i].length
#     1 <= m, n <= 10
#     -100 <= matrix[i][j] <= 100



class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Return all elements from the matrix when traversed in a spiral order.
        #   - Start at index [0, 0] -> Move right, then down, then left, then up.
        #   - Increment each edge inwards once we complete the loop (e.g. after first right pass, we can't reach row 0 again).

        res = []

        # Below variables represent the bounds of the traversal. They'll be incremented "inwards" as we traverse.
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # First, move right along the top row.
            for col in range(left, right + 1):
                res.append(matrix[top][col])
            top += 1

            # Move down along the right side.
            for row in range(top, bottom + 1):
                res.append(matrix[row][right])
            right -= 1

            # There's a chance that we're done traversing here -> terminate if left < right or top < bottom.
            if left > right or top > bottom:
                return res

            # Move left along the bottom row.
            for col in range(right, left - 1, -1):
                res.append(matrix[bottom][col])
            bottom -= 1

            # Move up along the left side.
            for row in range(bottom, top - 1, -1):
                res.append(matrix[row][left])
            left += 1

        return res

# Time Complexity: O(n * m) -> Visit every cell in matrix once.
# Space Complexity: O(1) -> No additional storage used.
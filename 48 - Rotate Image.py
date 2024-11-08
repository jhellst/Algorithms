# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:

# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]

# Example 2:

# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# Constraints:

#     n == matrix.length == matrix[i].length
#     1 <= n <= 20
#     -1000 <= matrix[i][j] <= 1000


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Modify the matrix. It needs to be rotated in-place.
        #   - This means that we need to "swap" positions of different elements in the matrix.

        # Process / Rules:
        #   - Flip the grid's values on x axis.
        #   - Then, traverse each row and swap that value with its mirrored value at row == col.

        n = len(matrix)

        for row in range(n):
            for col in range(n // 2): # Swap left side and right side values.
                matrix[row][col], matrix[row][n - col - 1] = matrix[row][n - col - 1], matrix[row][col]

        # Now, swap "across" -> Mirror across diagonal.
        for row in range(n):
            for col in range(n - row):
                # print("first_swap", matrix[row][col], "second_swap", matrix[n - col - 1][n - row - 1])
                matrix[row][col], matrix[n - col - 1][n - row - 1] = matrix[n - col - 1][n - row - 1], matrix[row][col]

# Time Complexity: O(m) -> Traverse and swap numbers in nums. 2 Separate swaps, but only traverse half of numbers each time.
# Space Complexity: O(1) -> No additional storage used.
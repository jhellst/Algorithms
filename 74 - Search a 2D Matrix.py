# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.


# Example 1:

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true

# Example 2:

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false


# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # The matrix can be flattened into a 1D matrix, then search via binary search.

        # matrix = [[cell for cell in row] for row in matrix]

        matrix = [val for row in matrix for val in row] # Flatten matrix to 1D.

        # Now, we can binary search the matrix.

        l, r = 0, len(matrix) - 1

        while l <= r:
            mid = (l + r) // 2
            curVal = matrix[mid]
            if curVal == target:
                return True
            elif curVal > target: # Current value too large -> search to the left.
                r = mid - 1
            else: # Current value too small -> search to the right.
                l = mid + 1

        return False


# Time Complexity: O(log(n * m)) -> Binary search of a 1D array of length n * m
# Space Complexity: O(1) -> no additional storage
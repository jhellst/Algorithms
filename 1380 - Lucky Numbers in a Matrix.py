# Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.
# A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

# Example 1:

# Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
# Output: [15]
# Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column.

# Example 2:

# Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
# Output: [12]
# Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.

# Example 3:

# Input: matrix = [[7,8],[1,2]]
# Output: [7]
# Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.

# Constraints:

# m == mat.length
# n == mat[i].length
# 1 <= n, m <= 50
# 1 <= matrix[i][j] <= 105.
# All elements in the matrix are distinct.


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:

        # Store the min/max values for each row/column. Planning to use 2 arrays.
        # Then, traverse each cell and append each that is the min/max of both row/column.

        row_min_values = [inf] * len(matrix)
        col_max_values = [-inf] * len(matrix[0])

        # Traverse row-by-row -> update row_min_values
        for row_index in range(len(matrix)):
            for col_index in range(len(matrix[0])):
                cur_val = matrix[row_index][col_index]

                if cur_val <= row_min_values[row_index]:
                    row_min_values[row_index] = cur_val


        # Traverse col-by-col -> update row_max_values
        for col_index in range(len(matrix[0])):
            for row_index in range(len(matrix)):
                cur_val = matrix[row_index][col_index]

                if cur_val >= col_max_values[col_index]:
                    col_max_values[col_index] = cur_val


        return [val for val in row_min_values if val in col_max_values]

# Time Complexity: O(n * m) -> Traverse every cell in the array twice.
# Space Complexity: O(n + m) -> Store min and max values (1 val for each row, 1 val for each column).
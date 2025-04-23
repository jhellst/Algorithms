# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Example 1:

# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

# Example 2:

# Input: grid = [[1]]
# Output: 4

# Example 3:

# Input: grid = [[1,0]]
# Output: 4

# Constraints:

# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        result = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    result += 4

                    if r > 0 and grid[r-1][c] == 1:
                        result -= 2

                    if c > 0 and grid[r][c-1] == 1:
                        result -= 2

        return result


# 2nd Solution:

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # DFS-style solution.
        # Key Details:
        #   - Only 1 island total -> we can use this to construct logic to count perimeter.
        #   - If 1) cell == 1, add perimeter.
        #       -> 1 neighbor, add 3
        #       -> 2 neighbors, add 2
        #       -> 3 neighbors, add 1
        #       -> 4 neighbors, add 0 (surrounded completely)

        def calculate_perimeter(row, col):
            perimeter_to_add = 4

            if row > 0 and grid[row - 1][col] == 1:
                perimeter_to_add -= 1
            if row < len(grid) - 1 and grid[row + 1][col] == 1:
                perimeter_to_add -= 1
            if col > 0 and grid[row][col - 1] == 1:
                perimeter_to_add -= 1
            if col < len(grid[0]) - 1 and grid[row][col + 1] == 1:
                perimeter_to_add -= 1
            return perimeter_to_add

        total_perimeter = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                # If cell == 1, calculate perimeter to add (check up, down, left, right).
                if grid[row][col] == 1:
                    total_perimeter += calculate_perimeter(row, col)

        return total_perimeter

# Time Complexity: O(n * m) -> Visit every cell in grid once.
# Space Complexity: O(1) -> No additional storage space used.

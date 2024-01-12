# https://leetcode.com/problems/max-increase-to-keep-city-skyline/description/

# There is a city composed of n x n blocks, where each block contains a single building shaped like a vertical square prism. You are given a 0-indexed n x n integer matrix grid where grid[r][c] represents the height of the building located in the block at row r and column c.
# A city's skyline is the outer contour formed by all the building when viewing the side of the city from a distance. The skyline from each cardinal direction north, east, south, and west may be different.
# We are allowed to increase the height of any number of buildings by any amount (the amount can be different per building). The height of a 0-height building can also be increased. However, increasing the height of a building should not affect the city's skyline from any cardinal direction.
# Return the maximum total sum that the height of the buildings can be increased by without changing the city's skyline from any cardinal direction.


# Example 1:


# Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
# Output: 35
# Explanation: The building heights are shown in the center of the above image.
# The skylines when viewed from each cardinal direction are drawn in red.
# The grid after increasing the height of buildings without affecting skylines is:
# gridNew = [ [8, 4, 8, 7],
#             [7, 4, 7, 7],
#             [9, 4, 8, 7],
#             [3, 3, 3, 3] ]
# Example 2:

# Input: grid = [[0,0,0],[0,0,0],[0,0,0]]
# Output: 0
# Explanation: Increasing the height of any building will result in the skyline changing.


# Constraints:

# n == grid.length
# n == grid[r].length
# 2 <= n <= 50
# 0 <= grid[r][c] <= 100



class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        # At the same time, we want to increase all buildings as much as possible -> but only while they are eligible to increase without changing the skyline from any direction.
        # The skyline changes when the outline changes (so from one direction, the max of each col/row is unchanged)
        # Keep a counter as you do this.

        # For steps, we want to find the max value of each row and column and store in a hashMap.

        maxRows = {}
        maxCols = {}

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                value = grid[r][c]
                maxRows[r] = max(maxRows.get(r, 0), value)
                maxCols[c] = max(maxCols.get(c, 0), value)

        increaseCount = 0

        # Now, we have the maxes of each spot. Traverse the grid once more and increase at each cell up to the minimum of maxRow and maxCol at that cell.
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                maxPossibleVal = min(maxRows[r], maxCols[c])
                increaseCount += maxPossibleVal - grid[r][c]

        return increaseCount

# Time Complexity: 2 * O(n^2) -> O(n^2) -> Need to traverse the entire grid 2 times, while the grid is n * n dimensions.
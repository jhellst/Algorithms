# You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the same row or on the same column.
# Return the number of servers that communicate with any other server.

# Example 1:
# Input: grid = [[1,0],[0,1]]
# Output: 0
# Explanation: No servers can communicate with others.

# Example 2:
# Input: grid = [[1,0],[1,1]]
# Output: 3
# Explanation: All three servers can communicate with at least one other server.

# Example 3:
# Input: grid = [[1,1,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,1]]
# Output: 4
# Explanation: The two servers in the first row can communicate with each other. The two servers in the third column can communicate with each other. The server at right bottom corner can't communicate with any other server.

# Constraints:
#     m == grid.length
#     n == grid[i].length
#     1 <= m <= 250
#     1 <= n <= 250
#     grid[i][j] == 0 or 1



class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Return the max_count of servers able to communicate with at least 1 other server.
        # First, add all x and y coords to a hashmap/set. Then, for each server, check if there are any other x or y coordinates that are equal.

        x_coords = {} # x_coord : count
        y_coords = {} # y_coord : count
        res = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    x_coords[row] = x_coords.get(row, 0) + 1
                    y_coords[col] = y_coords.get(col, 0) + 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    if x_coords[row] > 1 or y_coords[col] > 1:
                        res += 1

        return res

# Time Complexity: O(n * m) -> Loop through every cell of the grid 2 times.
# Space Complexity: O(n + m) -> Store coordinates of cells with servers -> In worst case, will need to store m + n coords.
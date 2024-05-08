# You are given an m x n grid rooms initialized with these three possible values.

# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

# Example 1:

# Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
# Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

# Example 2:

# Input: rooms = [[-1]]
# Output: [[-1]]

# Constraints:

# m == rooms.length
# n == rooms[i].length
# 1 <= m, n <= 250
# rooms[i][j] is -1, 0, or 231 - 1.


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        # BFS, starting from every gate. As we reach an valid cell, we insert the count (steps from origin).
        q = deque()

        rows, cols = len(rooms), len(rooms[0])
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append([r, c])

        # Now, we have all of the gate locations on the queue. BFS with these, while also keeping track of count.

        # When we look at a new cell, we ignore it if it's 1) a wall 2) already been visited.
        curLevel = 1
        while q:
            qLen = len(q)
            for _ in range(qLen):
                curR, curC = q.popleft()

                # Now, check adjacent squares. If they're valid empty rooms, append coords and change cell value to curLevel.
                directions = [[curR + 1, curC], [curR - 1, curC], [curR, curC + 1], [curR, curC - 1]]
                for r, c in directions:
                    if 0 <= r < rows and 0 <= c < cols and rooms[r][c] == 2147483647:
                        rooms[r][c] = curLevel
                        q.append([r, c])

            curLevel += 1 # Increment at the end, because the first cycle is just gates (not valid empty rooms).

# Time Complexity: O(2 * m * n) -> O(m * n) -> Traverse every cell in the array 2 times (once during initial scan, and once during BFS).
# Space Complexity: O(m * n) -> In worst case, every cell will be a "gate" and will be stored on the stack.
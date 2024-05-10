# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

# Example 1:

# Input: points = [[1,1],[2,2],[3,3]]
# Output: 3

# Example 2:

# Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4

# Constraints:

# 1 <= points.length <= 300
# points[i].length == 2
# -104 <= xi, yi <= 104
# All the points are unique.


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:

        # Need to populate a dict with slope:[point1, point2].

        # Pseudocode for solution:
        #   1) Loop through points. Sort to optimize and prevent recounting.
        #   2) For each point, calculate its slope with every other point.
        #   3) For any points where the slope is equal from the initial point, we can consider them both as members of the same line.

        points.sort()
        res = 0

        for i in range(len(points)):
            c = {} # Stores slope:count -> final count is +1 from this.
            maxCount = 0
            for j in range(i + 1, len(points)):

                yDiff = points[j][1] - points[i][1]
                xDiff = points[j][0] - points[i][0]

                if xDiff != 0:
                    slope = yDiff / xDiff
                else:
                    slope = "zero"
                yo
                c[slope] = c.get(slope, 0) + 1
                maxCount = max(maxCount, c[slope])

            res = max(res, maxCount)

        return res + 1

# Time Complexity: O(n * log(n)) + O(n^2) -> O(n^2)
# Space Complexity: O(n)
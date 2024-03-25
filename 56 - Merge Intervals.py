# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:

# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

# Example 2:

# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# Constraints:

# 1 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 104

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Want to merge all intervals where they overlap.
        # Need to sort the intervals, then merge them until either 1) no overlaps left or 2) 1 or less items on stack.

        stack = []
        intervals.sort()
        # print(intervals)

        for x, y in intervals:
            if not stack:
                stack.append((x, y))
            else:
                curX, curY = stack[-1]
                # If overlap, we want to merge the intervals.
                if x <= curY: # Overlap.
                    stack[-1] = (curX, max(y, curY))
                else:
                    stack.append((x, y))

        return stack

# Time Complexity: O(n) -> One pass of each interval in array.
# Space Complexity: O(n) -> Store up to each interval on stack.
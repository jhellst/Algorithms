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
        # Given a list of intervals (non-sorted), merge all overlaps and return the final list of intervals.
        intervals.sort()
        curStart, curEnd = intervals[0]
        res = [] # Contains intervals that have already been processed and added.

        for start, end in intervals[1:]:
            # Logic to determine if it overlaps with the currently stored interval.

            if start > curEnd:
                res.append([curStart, curEnd])
                curStart, curEnd = start, end
            elif end < curStart:
                res.append([start, end])
            else: # Some overlap. Combine the intervals and reassign curStart, curEnd to match the newly merged interval.
                curStart, curEnd = min(start, curStart), max(end, curEnd)

        res.append([curStart, curEnd]) # Append final interval.
        return res

# Time Complexity: O(n + n * log(n)) -> O(n * log(n)) -> Sort intervals array of length n, then single pass of intervals array.
# Space Complexity: O(1) -> No additional storage used.
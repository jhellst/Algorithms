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



# 2nd Solution:

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
                # Merge the intervals.
        #   - Sort the intervals
        #   - Then, merge any overlapping intervals as we traverse the array.
        #   - There will be a cur_interval that's being evaluated as we traverse the other intervals in the array.
        #   - We'll process the interval depending on if there is a merge, and if the interval has been passed over yet.

        res = []

        intervals.sort(key=lambda interval: (interval[0], interval[1])) # Sort intervals to be in order as they occur.
        cur_start, cur_end = intervals[0]

        # Possible conditions for intervals:
        #   1) cur_interval is BEFORE -> append cur_interval and replace cur_interval
        #   2) cur_interval is AFTER -> append new_interval and don't replace cur_interval (might not occur because of sorting)
        #   3) Overlap -> modify cur_interval to represent the new merged interval and move on.

        for start, end in intervals[1:]:
            if cur_end < start: # cur_interval is BEFORE.
                res.append([cur_start, cur_end])
                cur_start, cur_end = start, end
            elif cur_start > end: # cur_interval is AFTER.
                res.append([start, end])
            else: # Some overlap.
                cur_start, cur_end = min(start, cur_start), max(end, cur_end)
        res.append([cur_start, cur_end])

        return res

# Time Complexity: O(n * log(n)) -> Sort the intervals array and visit each interval once.
# Space Complexity: O(1) -> No additional storage used other than res.




# 2nd Solution:


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Merge the intervals.
        #   - Start with first interval, then "process" each consecutive interval.
        #   - Need to sort intervals, first.

        intervals.sort()
        res = []

        cur_start, cur_end = intervals[0]

        for start, end in intervals[1:]:
            if start > cur_end: # If next interval doesn't overlap -> Append current interval and continue.
                res.append([cur_start, cur_end])
                cur_start, cur_end = start, end
            else: # Some overlap of the intervals, so we need to merge them.
                cur_start = min(cur_start, start)
                cur_end = max(cur_end, end)

        if cur_start != None:
            res.append([cur_start, cur_end])
        return res

# Time Complexity: O(n + log(n)) -> Sort array of length n, then traverse the array once.
# Space Complexity: O(1) -> No additional storage space used.
# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]

# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

# Constraints:

# 0 <= intervals.length <= 104
# intervals[i].length == 2
# 0 <= starti <= endi <= 105
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 105


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Process the intervals as we traverse the array.
        # When there is overlap with newInterval, use different logic to "process" the interval.

        res = []

        for interval in intervals:
            if newInterval[0] > interval[1]: # newInterval does not overlap and comes later.
                res.append(interval)
            elif newInterval[1] < interval[0]: # newInterval does not overlap and comes before.
                res.append(newInterval)
                newInterval = interval
            else: # Some overlap.
                newInterval = [min(interval[0], newInterval[0]), max(interval[1], newInterval[1])]

        res.append(newInterval) # Append final interval to res.
        return res

# Time Complexity: O(n) -> Traverse every interval exactly 1 time.
# Space Complexity: O(1) -> No additional storage used.



# 2nd Solution:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Given a new interval, merge all overlapping time periods together.

        res = []

        for start, end in intervals:
            if end < newInterval[0]: # newInterval is after this interval -> append curInterval.
                res.append([start, end])
            elif start > newInterval[1]: # newInterval is before this interval -> append newInterval.
                res.append(newInterval)
                newInterval = [start, end]
            else: # Merging intervals -> Modify newInterval.
                newInterval = [min(start, newInterval[0]), max(end, newInterval[1])]

        res.append(newInterval)

        return res

# Time Complexity: O(n) -> Traverse intervals array 1 time.
# Space Complexity: O(1) -> No additional storage used.



# 3rd Solution:

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # We start with an unsorted array of non-overlapping intervals.
        # Want to add the new interval and merge, if necessary.
        #   - Traverse sorted intervals array
        #       -> Append cur_interval if it's been passed and assign new cur_interval
        #       -> Otherwise, modify cur_interval to "merge" the two overlapping intervals.
        #   - As a final step, append the final cur_interval before returning res.

        res = []
        intervals.sort()

        cur_interval = newInterval

        for start, end in intervals:
            if start > cur_interval[1]: # No overlap. cur_interval is before start and should be appended now.
                res.append(cur_interval)
                cur_interval = [start, end]
            elif end < cur_interval[0]: # No overlap. cur_interval is not reached yet.
                res.append([start, end])
            else: # Some overlap.
                cur_interval = [min(start, cur_interval[0]), max(end, cur_interval[1])]

        if cur_interval:
            res.append(cur_interval)

        return res

# Time Complexity: O(n) -> Traverse intervals array once.
# Space Complexity: O(1) -> No additional storage used.
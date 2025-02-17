# Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

# Example 1:

# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

# Example 2:

# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

# Example 3:

# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort the intervals, then iterate through them.
        # When the previous ending value is < current start, we need to remove the current interval (increment by 1).

        intervals.sort()

        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prevEnd: # Remove current interval if start is before prevEnd.
                res += 1
                prevEnd = min(prevEnd, end)
            else:
                prevEnd = end

        return res

# Time Complexity: O(n * log(n)) -> Sorted (O(log(n))) + traversal through sorted array (O(n))



class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Count how many "merge" actions are needed for the sorted range of intervals. That number is the number of removals needed.

        res = 0
        intervals.sort()

        prev_end = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prev_end: # No overlap, move on to next interval.
                prev_end = end
            else:
                res += 1
                prev_end = min(end, prev_end)

        return res

# Time Complexity: O(n*log(n)) -> Visit every interval in array after sorting.
# Space Complexity: O(1) -> No additional storage used.



# 2nd Solution:

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Greedy solution. We want to find out how many intervals would get merged.

        intervals.sort()
        count = 0

        prev_end = intervals[0][1]

        for start, end in intervals[1:]: # Determine if we merge cur_interval or continue.
            if start >= prev_end: # If no overlap.
                prev_end = end
            else: # Some overlap.
                prev_end = min(end, prev_end)
                count += 1

        return count

# Time Complexity: O(n) + O(log(n)) -> O(n) -> Visit every interval once.
# Space Complexity: O(1) -> No additional storage used.





# 3rd Solution:

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Find the minimum # of intervals that you need to remove to make them non-overlapping.
        # Greedy -> Sort the intervals, then remove every interval that would theoretically overlap.

        intervals.sort()
        prev_end = intervals[0][1]
        res = 0

        for start, end in intervals[1:]:
            if start >= prev_end: # No overlap.
                prev_end = end
            else: # Some overlap.
                prev_end = min(end, prev_end)
                res += 1

        return res

# Time Complexity: O(n * log(n)) -> Sort intervals and traverse array once.
# Space Complexity: O(1) -> No additional storage space used.
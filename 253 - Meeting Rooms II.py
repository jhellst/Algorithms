import heapq

# Given an array of meeting time intervals intervals where intervals[i] = [starti, endi], return the minimum number of conference rooms required.


# Example 1:

# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: 2

# Example 2:

# Input: intervals = [[7,10],[2,4]]
# Output: 1

# Constraints:

# 1 <= intervals.length <= 104
# 0 <= starti < endi <= 106


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        # We want to use a heap to hold each meeting occuring at any given time.
        # The heap only needs to hold ending time. Once we put it onto the heap, we don't need to know start time anymore.

        minHeap = []
        res = 0

        # First, sort intervals.
        intervals.sort()

        # We'll traverse the intervals, adding to minHeap.
        # When we reach a start value that is >= min value on the heap, we can pop from the heap and add the new end value (no overlap).
        # Otherwise, the current interval overlaps with every meeting still in the heap.

        for start, end in intervals:
            if minHeap:
                prevEnd = heapq.heappop(minHeap)
                if prevEnd <= start: # Latest interval to "end" does not overlap with new interval. Remove old interval from heap.
                    heapq.heappush(minHeap, end)
                else: # The intervals do overlap, add prevEnd back to heap and add new end.
                    heapq.heappush(minHeap, prevEnd)
                    heapq.heappush(minHeap, end)
            else:
                heapq.heappush(minHeap, end)

            res = max(res, len(minHeap))

        return res

# Time Complexity: O(n * log(n)) -> Sorting is O(n * log(n)) -> Heap is O(n * log(n))
# Space Complexity: O(n) -> Heap can contain every end value in intervals array.
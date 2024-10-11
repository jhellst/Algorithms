# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
#     For example, for arr = [2,3,4], the median is 3.
#     For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

# Implement the MedianFinder class:
#     MedianFinder() initializes the MedianFinder object.
#     void addNum(int num) adds the integer num from the data stream to the data structure.
#     double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.

# Example 1:

# Input
# ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
# [[], [1], [2], [], [3], []]
# Output
# [null, null, null, 1.5, null, 2.0]

# Explanation
# MedianFinder medianFinder = new MedianFinder();
# medianFinder.addNum(1);    // arr = [1]
# medianFinder.addNum(2);    // arr = [1, 2]
# medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
# medianFinder.addNum(3);    // arr[1, 2, 3]
# medianFinder.findMedian(); // return 2.0

# Constraints:

#     -105 <= num <= 105
#     There will be at least one element in the data structure before calling findMedian.
#     At most 5 * 104 calls will be made to addNum and findMedian.

# Follow up:

#     If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
#     If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?





class MedianFinder:
    # Median can either be 1) middle value of an odd-length list OR 2) avg. of middle 2 values of an even-length list.
    # For this reason, we need to use 2 heaps (1 min, 1 max) to store the 2 halves of the list.
    #   - Depending on the length, we'll calculate the median differently.
    # For addNum, we want to process it to "balance" the 2 heaps.

    def __init__(self):
        # Default to add to top when both lists are the same length.
        # Note: If there is an odd number of values, self.top will have the extra value.
        self.top = [] # min_heap
        self.bottom = [] # max_heap (need to use negative nums)

    def addNum(self, num: int) -> None:
        # Determine if the number is in the top_half or the bottom_half of values in the data stream.
        if not self.top:
            self.top.append(num)

        elif len(self.top) > len(self.bottom): # Bottom needs to gain a number.
            if num > self.top[0]:
                shift_num = heapq.heappop(self.top)
                heapq.heappush(self.bottom, -shift_num)
                heapq.heappush(self.top, num)
            else:
                heapq.heappush(self.bottom, -num)

        else: # Top needs to gain a number.
            if num < -self.bottom[0]:
                shift_num = -heapq.heappop(self.bottom)
                heapq.heappush(self.top, shift_num)
                heapq.heappush(self.bottom, -num)
            else:
                heapq.heappush(self.top, num)



    def findMedian(self) -> float:
        if len(self.top) > len(self.bottom):
            return self.top[0]
        else:
            return (self.top[0] - self.bottom[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()


# Time Complexity:
#   addNum: O(log(n)) -> Heap operation on heap of length n.
#   findMedian: O(1) -> Simple arithmetic.
# Space Complexity: O(n) -> Store each number on 1 of 2 heaps.
# Given an integer array nums and an integer k, return the kth largest element in the array.
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
# Can you solve it without sorting?


# Example 1:

# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5

# Example 2:

# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4


# Constraints:

# 1 <= k <= nums.length <= 105
# -104 <= nums[i] <= 104


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Find the kth largest element.
        # Use a minHeap to store values, pop until length of heap is k.

        heapq.heapify(nums)

        while len(nums) >= k:
            cur = heapq.heappop(nums)

        return cur

# Time Complexity: O(log(n)) -> Heap operations are log(n).
# Space Complexity: O(1) -> No additional storage needed.


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Solution using a minHeap.
        # As we add numbers, we only want to keep the k largest values in the heap. kth largest number will be on top of heap after operations are complete.

        minHeap = []
        for num in nums:
            heapq.heappush(minHeap, num)

            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return minHeap[0]

# Time Complexity: O(n * log(k)) -> For each num in nums, perform heap operations on heap of size k.
# Space Complexity: O(k) -> Store up to k items on the heap.


# 2nd Solution:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Return the kth largest element in the array.
        #   - We could sort, OR we can use a heap of length == k.
        #       -> More efficient.

        # Create a min_heap of size k -> we'll pop the smallest value off whenever size exceeds k.
        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]

# Time Complexity: O(n * log(k)) -> Traverse array of length n and conduct heap operations on heap of length k.
# Space Complexity: O(k) -> Store values on a heap of length k.


# 3rd Solution:

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Solution using a heap for optimal efficiency.

        min_heap = []
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]

# Time Complexity: O(n * log(k)) -> Traverse nums array and perform heap operations on a heap of length k.
# Space Complexity: O(k) -> Store up to k values on a min_heap.

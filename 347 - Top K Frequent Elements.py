# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1
# Output: [1]

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Find the top k most frequent elements. Generate hashmap from nums, then use a heap to store counts from hashmap.

        minHeap = []
        c = collections.Counter(nums)
        for key in c:
            heapq.heappush(minHeap, [c[key], key])
            if (len(minHeap) > k):
                heapq.heappop(minHeap) # Removes smallest value on minHeap, if the length is above k items.

        return [elem for [count, elem] in minHeap]

# Time Complexity: O(n * log(n)) -> Heap operations after adding every value in nums to the heap.
# Space Complexity: O(n + k) -> Place every value in nums on a heap. Create a counter with k unique elements.




# Solution 2:


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Return the k most frequent elements. We want to use a Counter and sort/heap. Heap is more efficient.

        min_heap = [] # [count, val]
        c = Counter(nums)

        for num in c:
            heapq.heappush(min_heap, [c[num], num]) # [count, val]
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return [num for count, num in min_heap]

# Time Complexity: O(n + n * log(k)) -> O(n * log(k)) -> Create a Counter, then traverse every key in the Counter and conduct heap operations on a heap of length k.
# Space Complexity: O(n + k) -> Store n elements in a Counter, and store k elements on a heap.



# 3rd Solution:

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Return the k most frequent elements.
        # Process: Create a counter for each key, and then push each [count, value] onto a min_heap.
        #   - Maintain min_heap size of k, and return ONLY the value from the remaining items on the heap.

        min_heap = []
        c = Counter(nums)
        for val in c:
            heapq.heappush(min_heap, [c[val], val])
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        res = [val for count, val in min_heap]
        return res

# Time Complexity: O(n * log(k)) -> Create a counter from every value in nums, and push/pop from heap of max size k.
# Space Complexity: O(n + k) -> Store up to n items in a counter/dict, and store up to k items in a heap.
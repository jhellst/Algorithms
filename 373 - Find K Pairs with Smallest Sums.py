# You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.
# Define a pair (u, v) which consists of one element from the first array and one element from the second array.
# Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

# Example 1:

# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Output: [[1,2],[1,4],[1,6]]
# Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

# Example 2:

# Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
# Output: [[1,1],[1,1]]
# Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

# Constraints:

# 1 <= nums1.length, nums2.length <= 105
# -109 <= nums1[i], nums2[i] <= 109
# nums1 and nums2 both are sorted in non-decreasing order.
# 1 <= k <= 104
# k <= nums1.length * nums2.length


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Use a heap to store [sum, pair].

        max_heap = []

        for n1 in nums1:
            for n2 in nums2:
                heapq.heappush(max_heap, [-n1 - n2, [n1, n2]])

                if len(max_heap) > k:
                    heapq.heappop(max_heap)

        # print(max_heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])

        return res


# 2nd Solution:

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Find the k smallest pairs, in terms of total sum of the 2 numbers.
        # Solution using a min_heap. Push [total_sum, [num1, num2]] to the heap.

        max_heap = [] # [-total_sum, [num1, num2]]

        for num1 in nums1:
            for num2 in nums2:
                heapq.heappush(max_heap, [-(num1 + num2), [num1, num2]])
                if len(max_heap) > k:
                    heapq.heappop(max_heap)

        return [pair for total_sum, pair in max_heap]

# Time Complexity: O(n * m * log(k)) -> Iterate through every combination between nums1 and nums2 and perform heap operations of a heap of length k.
# Space Complexity: O(k) -> Store up to k values on a heap.
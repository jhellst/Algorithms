# You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.
# For every i and j where 0 <= i < j < arr.length, we consider the fraction arr[i] / arr[j].
# Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where answer[0] == arr[i] and answer[1] == arr[j].

# Example 1:

# Input: arr = [1,2,3,5], k = 3
# Output: [2,5]
# Explanation: The fractions to be considered in sorted order are:
# 1/5, 1/3, 2/5, 1/2, 3/5, and 2/3.
# The third fraction is 2/5.

# Example 2:

# Input: arr = [1,7], k = 1
# Output: [1,7]

# Constraints:

# 2 <= arr.length <= 1000
# 1 <= arr[i] <= 3 * 104
# arr[0] == 1
# arr[i] is a prime number for i > 0.
# All the numbers of arr are unique and sorted in strictly increasing order.
# 1 <= k <= arr.length * (arr.length - 1) / 2

# Follow up: Can you solve the problem with better than O(n2) complexity?



class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # Note: arr is sorted in ascending order. For this reason, we can just loop twice starting at each index to ascend in fraction value.

        # Use a heap to store k smallest values.
        maxHeap = []

        for i, num in enumerate(arr):
            for j in range(len(arr) - 1, -1, -1):

                fraction = num / arr[j]
                heapq.heappush(maxHeap, [-fraction, (num, arr[j])])

                # If heap capacity is exceeded, pop from it.
                if len(maxHeap) > k:
                    heapq.heappop(maxHeap)

        return maxHeap[0][1]

# Time Complexity: O(n^2) -> Nested loop of every item in the array.
# Space Complexity: O(k) -> Store items on a heap of length k.
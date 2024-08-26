# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, return the k closest points to the origin (0, 0).
# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).
# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

# Example 1:


# Input: points = [[1,3],[-2,2]], k = 1
# Output: [[-2,2]]
# Explanation:
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

# Example 2:

# Input: points = [[3,3],[5,-1],[-2,4]], k = 2
# Output: [[3,3],[-2,4]]
# Explanation: The answer [[-2,4],[3,3]] would also be accepted.

# Constraints:

# 1 <= k <= points.length <= 104
# -104 <= xi, yi <= 104

import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Return the k closest points to the origin, based on distance.
        # Use the distance formula and push [distance, point] to a heap. Use heap operations to keep k items on the heap.

        maxHeap = []

        for x, y in points:
            distance = sqrt(x**2 + y**2)
            heapq.heappush(maxHeap, [-distance, [x, y]])

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [point for distance, point in maxHeap]

# Time Complexity: O(n + nlog(k)) -> O(n*log(k)) -> Traverse array of size n and conduct heap operations on a heap of length k.
# Space Complexity: O(k) -> Store up to k elements on maxHeap.




# Solution #2:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Store points on a max_heap.

        max_heap = [] # [distance, point]

        for point in points:
            distance = sqrt(point[0]**2 + point[1]**2)
            heapq.heappush(max_heap, [-distance, point])

            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [point for distance, point in max_heap]

# Time Complexity: O(n * log(k)) -> Traverse array of length n and conduct heap operations on heap of length k.
# Space Complexity: O(k) -> Store k items in max_heap.


# 2nd Solution:

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Use a heap to efficiently store the closest k points, in terms of distance to origin.
        max_heap = [] # [distance, point]

        for x, y in points:
            distance = sqrt(x**2 + y**2)
            heapq.heappush(max_heap, [-distance, [x, y]])
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [points for distance, points in max_heap]

# Time Complexity: O(n * log(k)) -> Traverse points array of length n and perform heap operations on heap of length k.
# Space Complexity: O(k) -> Store points on a heap of length k.
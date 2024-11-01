# You are given an array of integers stones where stones[i] is the weight of the ith stone.
# We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

# If x == y, both stones are destroyed, and
# If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
# At the end of the game, there is at most one stone left.

# Return the weight of the last remaining stone. If there are no stones left, return 0.

# Example 1:

# Input: stones = [2,7,4,1,8,1]
# Output: 1
# Explanation:
# We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
# we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
# we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
# we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of the last stone.

# Example 2:

# Input: stones = [1]
# Output: 1

# Constraints:

# 1 <= stones.length <= 30
# 1 <= stones[i] <= 1000


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use a max_heap. We pop 2 stones at a times and "smash" them until there is only 1 stone on the heap.

        def combine_stones(first, second):
            if first == second:
                return None
            else:
                return first - second


        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)

        while len(max_heap) >= 2:
            first = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)

            new_stone = combine_stones(-first, -second)
            if new_stone:
                heapq.heappush(max_heap, -new_stone)

        if not max_heap:
            return 0
        return -max_heap[0]


# Time Complexity: O(n * log(n)) -> Heap operations on heap of length n.
# Space Complexity: O(n) -> N items stored on a max_heap.




# 2nd Solution:

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Use a max_heap. We can pop two stones at a time and "smash" them together.
        #   - If 2 stones are equal, destroy both. Otherwise, re-append 1 stone with val == abs(y - x).

        max_heap = [- s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            # Pop 2 stones and smash them together.
            stone_1 = -heapq.heappop(max_heap)
            stone_2 = -heapq.heappop(max_heap)

            if stone_1 != stone_2:
                new_val = abs(stone_1 - stone_2)
                heapq.heappush(max_heap, -new_val)

        if not max_heap:
            return 0
        return -max_heap[0]

# Time Complexity: O(n * log(n)) -> Conduct heap operations on heap of length n.
# Space Complexity: O(n) -> Store n values on heap.
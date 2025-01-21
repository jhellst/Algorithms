# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.
# Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that she can eat all the bananas within h hours.


# Example 1:

# Input: piles = [3,6,7,11], h = 8
# Output: 4
# Example 2:

# Input: piles = [30,11,23,4,20], h = 5
# Output: 30
# Example 3:

# Input: piles = [30,11,23,4,20], h = 6
# Output: 23


# Constraints:

# 1 <= piles.length <= 104
# piles.length <= h <= 109
# 1 <= piles[i] <= 109


import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Koko can eat k bananas from each pile (in any given scenario where rate is k).
        # Binary search of the RATE of bananas eaten. We rate will be between 1 and max(piles).

        left, right = 1, max(piles)
        res = right # Right is max possible rate and is valid.

        while left <= right:
            mid = (left + right) // 2

            # Now, we process Koko's eating process to see how long it takes.
            hoursTaken = 0
            for pile in piles: # How many hours taken by Koko to eat EACH pile?
                hoursTaken += math.ceil(pile / mid)

            if hoursTaken <= h: # Valid answer. Continue searching lower rates for valid answers.
                res = mid
                right = mid - 1
            else:
                left = mid + 1

        return res


# Time Complexity: O( n * log(m) ) -> Binary search (O(log(m))) of rates from 1 to m. For each binary search, need to traverse entire piles array ( O(n) ) to calculate timeTaken.
# Space Complexity: O(1) -> No additional storage used (Besides hoursTaken varible ( O(1)) ).





# 2nd Solution:

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Binary search solution. We want to search to find the minimum eating rate K that will still "eat" all of the bananas in time.

        min_rate = max(piles)
        left, right = 1, max(piles)
        total_bananas = sum(piles)

        while left <= right:
            mid = (left + right) // 2

            hours_taken = 0
            for pile in piles:
                hours_taken += math.ceil(pile / mid)
            if hours_taken > h:
                left = mid + 1
            else:
                min_rate = min(min_rate, mid)
                right = mid - 1

        return min_rate

# Time Complexity: O(n * log(m)) -> Binary search of array of length n, for range of 1 to m (max value of piles).
# Space Complexity: O(1) -> No additional storage used.
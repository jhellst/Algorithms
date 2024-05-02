# Given an integer array nums that does not contain any zeros, find the largest positive integer k such that -k also exists in the array.
# Return the positive integer k. If there is no such integer, return -1.

# Example 1:

# Input: nums = [-1,2,-3,3]
# Output: 3
# Explanation: 3 is the only valid k we can find in the array.

# Example 2:

# Input: nums = [-1,10,6,7,-7,1]
# Output: 7
# Explanation: Both 1 and 7 have their corresponding negative values in the array. 7 has a larger value.

# Example 3:

# Input: nums = [-10,8,6,7,-2,-3]
# Output: -1
# Explanation: There is no a single valid k, we return -1.

# Constraints:

# 1 <= nums.length <= 1000
# -1000 <= nums[i] <= 1000
# nums[i] != 0


class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        # Find the max int that has its inverse in the array.
        # Traverse nums, storing each number in a set. When we are at a # where its inverse is in the set, we can compare that to res.

        res = -1

        seen = set()

        for num in nums:
            if -num in seen:
                res = max(res, abs(num))
            seen.add(num)

        return res

# Time Complexity: O(n) -> Single pass of array of length n.
# Space Complexity: O(n) -> In worst case, store every value in nums in a set.
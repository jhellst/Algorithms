# Given an integer array nums of length n where all the integers of nums are in the range[1, n] and each integer appears at most twice, return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant auxiliary space, excluding the space needed to store the output

# Example 1:
# Input: nums = [4, 3, 2, 7, 8, 2, 3, 1]
# Output: [2, 3]

# Example 2:
# Input: nums = [1, 1, 2]
# Output: [1]

# Example 3:
# Input: nums = [1]
# Output: []


# Constraints:
#     n == nums.length
#     1 <= n <= 105
#     1 <= nums[i] <= n
#     Each element in nums appears once or twice.


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = set()
        seen = set()

        for num in nums:
            if num in seen:
                res.add(num)
            else:
                seen.add(num)

        return [val for val in res]

# Time Complexity: O(n) -> Traverse nums exactly once.
# Space Complexity: O(n) -> Store up to n values in seen set.

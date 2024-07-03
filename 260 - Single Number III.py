# Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.
# You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

# Example 1:

# Input: nums = [1,2,1,3,2,5]
# Output: [3,5]
# Explanation:  [5, 3] is also a valid answer.

# Example 2:

# Input: nums = [-1,0]
# Output: [-1,0]

# Example 3:

# Input: nums = [0,1]
# Output: [1,0]

# Constraints:

# 2 <= nums.length <= 3 * 104
# -231 <= nums[i] <= 231 - 1
# Each integer in nums will appear twice, only two integers will appear once.


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # Use a set. Traverse nums array, adding each number to the set.
        # When a number is already contained in the set, remove it if/when we see it again.
        # Return the remaining values in the set -> they were only observed once.

        num_set = set()

        for num in nums:
            if num in num_set:
                num_set.remove(num)
            else:
                num_set.add(num)

        return num_set

# Time Complexity: O(n) -> Traverse nums array 1 time.
# Space Complexity: O(n) -> Store up to every number once in num_set.
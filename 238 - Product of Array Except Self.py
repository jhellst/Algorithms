# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]

# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Must run in O(n) time, so looking for a single-pass solution.
        # Intuition is to use a prefix-product and postfix-product, and recalculate these as we traverse the array.

        res = [1] * len(nums)
        prefixes = [1] * len(nums)
        postfixes = [1] * len(nums)

        # First populate prefix products while traversing nums.
        prefix = 1
        for i, num in enumerate(nums):
            prefixes[i] = prefix
            prefix *= num

        postfix = 1
        # Then, populate postfix products while traversing nums backwards.
        for i in range(len(nums) - 1, -1, -1):
            postfixes[i] = postfix
            postfix *= nums[i]

        # Final Step: Traverse the array and calculate from product of prefix and postfix at that index.
        for i in range(0, len(nums)):
            res[i] = prefixes[i] * postfixes[i]

        return res

# Time Complexity: O(n) -> Traverse the array three times.
# Space Complexity: O(n) -> Store prefixes and postfixes in array of length n.
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:

# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:

# Input: nums = [2,0,1]
# Output: [0,1,2]

# Constraints:

# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Want to reorder the list 0 -> 1 -> 2

        if len(nums) < 2:
            return nums

        num_counts = [0, 0, 0] # Counts for 0, 1, 2 values.
        for num in nums:
            num_counts[num] += 1

        insert_index = 0
        for i, num in enumerate(num_counts):
            for count in range(num_counts[i]):
                nums[insert_index] = i
                insert_index += 1

        return nums

# Time Complexity: O(n) -> Pass over array twice (1 time to get counts of 0/1/2, 1 time to reassign values)
# Space Complexity: O(n) -> Store every value in a separate array. Max size of array is n (each value in nums is unique).
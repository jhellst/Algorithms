# here is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4

# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1

# Example 3:

# Input: nums = [1], target = 0
# Output: -1

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Array is sorted but rotated (minimum value can be at any index).
        # Binary search, but need to use additional processing logic to ensure that we're searching on the correct "side".

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target: # Mid is too large, we want to search for a smaller number.
                if nums[mid] >= nums[left] and target < nums[left]: # Mid is part of left side AND target is less than left. Search right for target.
                    left = mid + 1
                else:
                    right = mid - 1

            else: # Mid is too small, search for a larger number.
                if nums[mid] <= nums[right] and target > nums[right]: # Mid is part of right side AND target is greater than right. Search left for target.
                    right = mid - 1
                else:
                    left = mid + 1

        return -1

# Time Complexity: O(log(n)) -> Binary search of an array of size n.
# Space Complexity: O(1) -> No additional storage used.
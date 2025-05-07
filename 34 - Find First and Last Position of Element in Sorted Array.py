# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.

# Example 1:
# Input: nums = [5, 7, 7, 8, 8, 10], target = 8
# Output: [3, 4]

# Example 2:
# Input: nums = [5, 7, 7, 8, 8, 10], target = 6
# Output: [-1, -1]

# Example 3:
# Input: nums = [], target = 0
# Output: [-1, -1]


# Constraints:
#     0 <= nums.length <= 105
#     -109 <= nums[i] <= 109
#     nums is a non-decreasing array.
#     -109 <= target <= 109


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # Binary search. We need to perform 2 separate searches -> far left and far right index.

        left, right = 0, len(nums) - 1
        left_index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                left_index = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        left, right = 0, len(nums) - 1
        right_index = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                right_index = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return [left_index, right_index]

# Time Complexity: O(log(n)) -> Binary search for index in array twice.
# Space Complexity: O(1) -> No additional storage used.

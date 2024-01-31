# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.


# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
# Example 2:

# Input: nums = [4,5,6,7,0,1,2]
# Output: 0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
# Example 3:

# Input: nums = [11,13,15,17]
# Output: 11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.


# Constraints:

# n == nums.length
# 1 <= n <= 5000
# -5000 <= nums[i] <= 5000
# All the integers of nums are unique.
# nums is sorted and rotated between 1 and n times.


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # The array is sorted, but rotated so that (unless no shift) the lowest element will be directly to the right of the highest element.
        # Binary search-style solution, but with additional steps to search on the correct side, given the left/right values of the current window.
        # Solution will be the minimum element. We want to binary search for minimum and then terminate and return that number.

        left, right = 0, len(nums) - 1
        minValue = nums[0]

        while left <= right:
            # To find which "half" has the minimum, we want to check if mid > left (in which case mid is part of the left portion).
            mid = (left + right) // 2
            minValue = min(minValue, nums[mid])

            if nums[mid] > nums[right]: # Min is on right side.
                left = mid + 1
            else:
                right = mid - 1

        return minValue

# Time Complexity: O(log(n)) -> Binary search of a single array.
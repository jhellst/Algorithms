# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

# Constraints:

# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Array is already sorted, so we can search using 2 pointers.
        # Converge on target.
        # Note that array is 1-indexed, so add 1 to each value in return array.

        left, right = 0, len(numbers) - 1
        while left < right:
            curSum = numbers[left] + numbers[right]
            if curSum == target:
                return [left + 1, right + 1]
            elif curSum > target: # Sum too high -> increment down from right side to reduce sum.
                right -= 1
            else:
                left += 1

# Time Complexity: O(n) -> Single pass with 2 pointers.
# Space Complexity: O(1) -> No additional storage used.



class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Sorted array -> we need to converge on a sum that matches.
        #   - There is guaranteed exactly 1 solution.
        #   - 1-indexed (so need to add 1 to indexes in returned value)

        # Solution using 2 pointers. We start at both ends with a cur_sum, then increment from left if sum is too low and from right if sum is too high.

        left, right = 0, len(numbers) - 1
        while True:
            cur_sum = numbers[left] + numbers[right]
            if cur_sum == target:
                return [left + 1, right + 1]
            elif cur_sum > target:
                right -= 1
            else:
                left += 1

# Time Complexity: O(n) -> Traverse each number up to once.
# Space Complexity: O(n) -> No additional storage used.
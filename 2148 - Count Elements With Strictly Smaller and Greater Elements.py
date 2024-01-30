# Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.


# Example 1:

# Input: nums = [11,7,2,15]
# Output: 2
# Explanation: The element 7 has the element 2 strictly smaller than it and the element 11 strictly greater than it.
# Element 11 has element 7 strictly smaller than it and element 15 strictly greater than it.
# In total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.
# Example 2:

# Input: nums = [-3,3,3,90]
# Output: 2
# Explanation: The element 3 has the element -3 strictly smaller than it and the element 90 strictly greater than it.
# Since there are two elements with the value 3, in total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.


class Solution:
    def countElements(self, nums: List[int]) -> int:
        # Find min and max values of the array.
        # Then, traverse the array, incrementing res if it is not equal to min or max.

        minimum = min(nums)
        maximum = max(nums)
        res = 0

        # Now, traverse again -> increment res by 1 each time the number isn't equal to min or max.

        for num in nums:
            if num != minimum and num != maximum:
                res += 1

        return res

# Time Complexity: O(n) -> O(n) to find min and max, O(n) to traverse array 1 time.
# Space compleity: O(1) -> No additional space.
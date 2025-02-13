# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true

# Example 2:

# Input: nums = [1,2,3,4]
# Output: false

# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

# Constraints:

# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use a set. If current number is already in set, return True.
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

# Time Complexity: O(n) -> Single pass of array.
# Space Complexity: O(n) -> Store up to every value in set 1 time.




# 2nd Solution:

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Use a set. If cur_num is already in the set, return True.

        num_set = set()
        for num in nums:
            if num in num_set:
                return True
            num_set.add(num)

        return False

# Time Complexity: O(n) -> In worst case, visit every value in nums one time.
# Space Complexity: O(n) -> In worst case, store every value in nums in a set.
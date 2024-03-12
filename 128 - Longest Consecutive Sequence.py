# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

# Example 2:

# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9

# Constraints:

# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # O(n) time, so single-pass.
        # We want to add all numbers to a set, then we want to Check the consecutive numbers in the set.

        numSet = set(nums)
        maxLength = 0

        for num in numSet:
            if (num - 1) not in numSet: # Ensure that we're not starting from the middle of a sequence.
                curLength = 1
                while (num + curLength in numSet):
                    curLength += 1
                maxLength = max(curLength, maxLength)

        return maxLength

# Time Complexity: O(n) -> Single pass of every number in array.
# Space Complexity: O(n) -> Store up to every number once in a set.
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



# 2nd Solution:

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Return the length of the longest consecutive sequence.
        #   - Use a set to store all nums.
        #   - Then, iterate through each num in nums, checking for the existence of a consecutive sequence (and incrementing accordingly).
        #   - Note: We can ignore evaluating any nums where num - 1 is is the set.

        if not nums:
            return 0

        max_length = 1

        num_set = set(nums)
        for num in num_set:
            if (num - 1) not in num_set:
                cur_length = 1
                while (num + cur_length) in num_set:
                    cur_length += 1
                    max_length = max(max_length, cur_length)

        return max_length

# Time Complexity: O(n) -> Convert nums array to a set of max_size = n. Then, visit every number in num_set once.
# Space Complexity: O(n) -> Store every num in nums in num_set.



# 2nd Solution:

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # We need to find length of the longest consecutive sequence within the array. Numbers can be in any order, as long as they are sequential in value.
        # Store all values in nums into a set. Then, check each value for length of sequence. If val - 1 exists in num_set, we can ignore it (we'll count from the beginning of the sequence).

        num_set = set(nums)
        max_length = 0

        for num in num_set:
            if (num - 1) not in num_set:
                cur_length = 1
                while (num + cur_length) in num_set:
                    cur_length += 1
                max_length = max(max_length, cur_length)

        return max_length

# Time Complexity: O(n) -> Create set of size n, and loop through each value in num_set 1 time.
# Space Complexity: O(n) -> Store n values in a set.
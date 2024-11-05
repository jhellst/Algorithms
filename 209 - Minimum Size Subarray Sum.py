# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# Example 1:

# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem constraint.

# Example 2:

# Input: target = 4, nums = [1,4,4]
# Output: 1

# Example 3:

# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0

# Constraints:

#     1 <= target <= 109
#     1 <= nums.length <= 105
#     1 <= nums[i] <= 104

# Follow up: If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log(n)).


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Return the min_length of the subarray whose sum is >= target.
        # Sliding window solution:
        #   - If sum >= target, we can compare to res AND start the decrement the window inwards from the left.

        if sum(nums) < target:
            return 0

        res = inf # Length.

        left, right = 0, 0
        cur_sum = 0

        while right < len(nums) or cur_sum >= target:
            # First, compare current window. While sum is lower than target, continue to expand right side.
            while cur_sum < target and right < len(nums):
                cur_sum += nums[right]
                right += 1

            # Now, we can decrement from left to check for shorter ranges.
            while cur_sum >= target and left < right:
                cur_sum -= nums[left]
                left += 1

            # Now, we have a potentially valid sum that's been minimized in length (locally).
            # if cur_sum >= target:
            res = min(res, right - left + 1)

        if res == inf:
            return 0
        return res

# Time Complexity: O(n) -> 2 Pointers traverse nums array up to once each.
# Space Complexity: O(1) -> No additional storage used.